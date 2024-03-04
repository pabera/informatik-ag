import picamera
import time
import shutil

# Pi Kamera initialisieren
camera = picamera.PiCamera()

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
            filename = time.strftime("%Y%m%d-%H%M%S") + '.jpg'
            camera.capture(filename)
            # print(f"Photo taken and saved as {filename}")

            # Dupliziere das Bild als `vogalcam.jpg`
            shutil.copyfile(filename, 'vogalcam.jpg')
        except Exception as e:
            print(f"Es is ein Fehler aufgetreten: {e}")

        # Warte
        time.sleep(5)
finally:
    # Wenn das Programm beendet wird, soll die Kamera korrekt beendet werden
    camera.close()
