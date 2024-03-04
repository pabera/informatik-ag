import picamera
import time
import shutil
import os

# Name des Ordners, in den die Bilder gespeichert werden
output_dir = "output"

# Überprüfe, ob der Ordner existiert, wenn nicht, wird er erstellt
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Pi Kamera initialisieren
camera = picamera.PiCamera()
# Interval, aller wieviel sekunden das Foto gemacht werden soll
# Sollte nicht kleiner gleich 3 sein
interval = 5
# Präfix der Fotos
prefix = 'vogelcam'

try:
    while True:
        # Foto Auflösung
        camera.resolution = (1024, 768)

        # Optional: Wenn die Kamera nicht hell genug ist, kann man den ISO Wert anpassen
        # camera.iso = 800

        # Erlaube der Kamera sich an die Lichtverhältnisse anzupassen
        time.sleep(2)

        try:
            # Foto aufnehmen mit aktuellem Zeitstempel
            filename = os.path.join(output_dir, prefix + '-' + time.strftime("%Y%m%d-%H%M%S") + '.jpg')
            camera.capture(filename)
            # print(f"Foto aufgenommen und als {filename} gespeichert")

            # Dupliziere das Bild als `vogalcam.jpg` im "output" Verzeichnis
            shutil.copyfile(filename, os.path.join(output_dir, prefix + '.jpg'))
        except Exception as e:
            print(f"Es is ein Fehler aufgetreten: {e}")

        # Warte
        time.sleep(interval)
finally:
    # Wenn das Programm beendet wird, soll die Kamera korrekt beendet werden
    camera.close()
