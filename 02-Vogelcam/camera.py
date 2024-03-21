import picamera
import time
import os
import boto3
import yaml

# Setze Verzeichnis des Script als Arbeitsverzeichnis
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Konfigurationsdatei einlesen
with open('../config.yml', 'r') as file:
    config = yaml.safe_load(file)

# AWS-Zugangsdaten direkt im Skript (nicht empfohlen für den Produktiveinsatz!)
aws_access_key_id = config['aws']['access_key_id']
aws_secret_access_key = config['aws']['secret_access_key']
region_name = config['aws']['region_name']
# S3 Bucket-Details
bucket_name = config['aws']['bucket_name']
# Kamera Einstellungen
resolution_x = config['camera']['resolution']['x']
resolution_y = config['camera']['resolution']['y']
interval = config['camera']['interval']
prefix = config['camera']['prefix']                 # Präfix der Foto Dateien
output_dir = config['camera']['output_dir']         # Name des Ordners, in den die Bilder gespeichert werden

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
    except Exception as e:
        print(f"Fehler beim Hochladen nach S3: {e}")

# Überprüfe, ob der Ordner existiert, wenn nicht, wird er erstellt
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Pi Kamera initialisieren
camera = picamera.PiCamera()
camera.resolution = (resolution_x, resolution_y)
time.sleep(2)  # Erlaube der Kamera, sich an die Lichtverhältnisse anzupassen

try:
    while True:
        try:
            start_time = time.time()

            filename = os.path.join(output_dir, prefix + '.jpg')
            camera.capture(filename)

            # Das aktuellste Foto zweimal auf S3 hochladen, einmal mit einem Timestamp Namen
            upload_to_s3(filename, bucket_name, object_name=prefix + '-' + time.strftime("%Y%m%d-%H%M%S") + '.jpg')
            # Und einmal als vogelcam.jpg
            upload_to_s3(filename, bucket_name)

            # Berechnung der verstrichenen Zeit und Anpassung des Wartintervals
            elapsed_time = time.time() - start_time
            adjusted_sleep = max(0, interval - elapsed_time)
            time.sleep(adjusted_sleep)

        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")

finally:
    camera.close()
