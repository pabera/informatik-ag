import picamera
import pathlib

# Voreinstellungen
width=320
height=240

# Kamera initialisieren
camera = picamera.PiCamera()
camera.vflip = False
camera.hflip = False
camera.brightness = 60
camera.resolution = (width, height)

current_path = pathlib.Path(__file__).parent.resolve()
photo_name = f'{current_path}/camera.jpg'
camera.capture(photo_name)

print('Foto aufgenommen')
camera.close()
