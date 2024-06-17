# Stop-Motion with ffmpeg

## Schritt 1: Bilder für FFMPEG vorbereiten

Stelle sicher, dass deine Bilder numerisch sortiert sind (zum Beispiel `img001.jpg`, `img002.jpg`, `img003.jpg`, usw.). FFMPEG wird diese Reihenfolge nutzen, um den Film zu erstellen.

## Schritt 2: Stop-Motion-Film erstellen

1. Öffne das Terminal und navigiere zum Ordner, der deine Bilder enthält:

   ```bash
   cd /pfad/zu/deinem/bilderordner
   ```

   Ersetze `/pfad/zu/deinem/bilderordner` mit dem tatsächlichen Pfad.

2. Verwende den folgenden FFMPEG-Befehl, um die Bilder zu einem Film zusammenzufügen. Hier kannst du auch die Bildrate (fps - frames per second) anpassen, um die Abstände zwischen den Bildern zu konfigurieren:

   ```bash
   ffmpeg -r 10 -pattern_type glob -i '*.jpg' -c:v libx264 -pix_fmt yuv420p stop_motion_film.mp4
   ```

   - `-r 10`: Setzt die Bildrate auf 10 Bilder pro Sekunde. Du kannst diesen Wert ändern, um die Geschwindigkeit des Films zu beeinflussen.
   - `-pattern_type glob`: Ermöglicht die Nutzung von Glob-Mustern beim Auswählen der Dateien.
   - `-i '*.jpg'`: Wählt alle JPG-Dateien im Ordner aus. Achte darauf, dass deine Dateiendung zu deinen Bildern passt (z.B. `.png` oder `.jpeg`).
   - `-c:v libx264`: Verwendet den H.264 Codec für das Video.
   - `-pix_fmt yuv420p`: Stellt ein gängiges Pixelformat für die Videoausgabe sicher.
   - `stop_motion_film.mp4`: Der Name der Ausgabedatei.

3. Drücke Enter, um den Befehl auszuführen. FFMPEG wird die Bilder zu einem Video zusammenfügen, das in der Datei `stop_motion_film.mp4` gespeichert wird.

## Schritt 3: Überprüfung

Überprüfe die erzeugte Datei `stop_motion_film.mp4` in deinem Bilderordner. Du kannst sie mit jedem Standard-Videoplayer abspielen, um sicherzustellen, dass dein Stop-Motion-Film wie gewünscht aussieht.

Das sind die grundlegenden Schritte, um mit FFMPEG auf einem Mac einen Stop-Motion-Film aus Bildern zu erstellen. Experimentiere mit verschiedenen Bildraten, um den perfekten Effekt für deinen Film zu finden!
