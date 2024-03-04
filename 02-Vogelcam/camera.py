import picamera
import time
import os
import boto3

# AWS-Zugangsdaten direkt im Skript (nicht empfohlen für den Produktiveinsatz!)
aws_access_key_id = 'DEIN_ACCESS_KEY'
aws_secret_access_key = 'DEIN_SECRET_KEY'
region_name = 'eu-central-1'
# S3 Bucket-Details
bucket_name = 'DEIN_BUCKET_NAME'

# Initialisiere einen boto3-Client mit expliziten AWS-Zugangsdaten
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

def upload_to_s3(file_path, bucket_name, object_name=None):
    """
    Lädt eine Datei in einen S3-Bucket hoch

    :param file_path: Dateipfad der hochzuladenden Datei
    :param bucket_name: Ziel-Bucket
    :param object_name: S3-Objektname. Wenn nicht angegeben, wird file_path verwendet
    """
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        response = s3.upload_file(file_path, bucket_name, object_name)
        # print(f"Hochgeladen {file_path} nach s3://{bucket_name}/{object_name}")
    except Exception as e:
        print(f"Fehler beim Hochladen nach S3: {e}")

# Name des Ordners, in den die Bilder gespeichert werden
output_dir = "tmp_output"

# Überprüfe, ob der Ordner existiert, wenn nicht, wird er erstellt
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Pi Kamera initialisieren
camera = picamera.PiCamera()
# Intervall in Sekunden, sollte 3 Sek nicht unterschreiten
interval = 5
# Präfix der Foto Dateien
prefix = 'vogelcam'

try:
    while True:
        time.sleep(2)  # Erlaube der Kamera, sich an die Lichtverhältnisse anzupassen

        try:
            filename = os.path.join(output_dir, prefix + '-' + time.strftime("%Y%m%d-%H%M%S") + '.jpg')
            camera.capture(filename)

            # Das aktuellste Foto zweimal auf S3 hochladen, einmal mit dem Originalnamen
            upload_to_s3(filename, bucket_name)
            # Und einmal als vogelcam.jpg
            upload_to_s3(filename, bucket_name, object_name=prefix + '.jpg')
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")

        time.sleep(interval)
finally:
    camera.close()
