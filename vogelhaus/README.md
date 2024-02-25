# Nistkasten mit Kamera

## Raspberry Pi vorbereiten

1. SD Karte beschreiben
    1. Stecke die SD Karte in den SD-Karten-Leser im Computer
    1. Öffne das Programm Raspberry Pi Imager
    1. Wähle folgenden Einstellungen
        * Raspberry Pi Device:
            * Raspberry Pi 3
            * Raspberry Pi Zero 2 W
        * Operating System:
            * Wähle *Raspberry Pi OS (other)*
            * Dann, wähle *Raspberry Pi OS (Legacy, 32-Bit) Lite*
        * Storage: Wähle die SD Karte aus (es gibt nur eine Möglichkeit)
    1. Klicke *Next*
    1. Klicke *Edit Settings*
        * Verändere den *Hostname*: `vogelcamX` -> Ändere das `X` zu einer beliebigen Zahl
        * Wähle ein *Password*
        * Stelle die richtigen WLAN Einstellungen
        * Klicke *Save*
    1. Klicke *Yes*
    1. Klicke *Yes*
    1. Computer-Passwort muss eingegeben werden
    1. Nun wird das Betriebssystem auf der SD Karte installiert
    1. Wenn die Installation abgeschlossen ist, klicke *Continue*
1. Entferne die SD Karte aus dem SD-Karten-Leser
1. SD Karte in Raspberry Pi einsetzen
1. Raspberry Pi an Strom anschließen und hochfahren
1. Mit `ssh` auf Raspberry Pi einloggen
    1. Auf dem Computer, öffne ein Terminal
    1. Befehl eingeben: `ssh meise@vogelcamX.local` (Denke daran, das X mit der Zahl zu ersetzen)
    1. Es kann sein, dass du folgende Frage siehst
        * `Are you sure you want to continue connecting (yes/no/[fingerprint])?`
        * Dann schreibe `yes` und drücke *Eingabe* / *Enter*
    1. Als nächstes wirst du nach deinem Passwort gefragt
1. Wenn du eingeloggt bist, musst du als nächstes die Raspberry Pi Einstellungen aufrufen
    1. Befehl eingeben: `sudo raspi-config`
    1. Navigiere mit den Pfeiltasten zum Punkt 3: `Interfacing Options`
    1. Ändere `Legacy Camera` zu `Yes`
    1. Einstellungen verlassen: `Esc` drücken
1. Raspberry Pi neustarten:
    1. Befehl eingeben: `sudo reboot`

## Kamera Software vorbereiten

1. Nach dem Neustart, musst du dich wieder auf mit `ssh` auf Raspberry Pi einloggen
    1. Öffne ein Terminal
    1. Befehl eingeben: `ssh meise@vogelcam.local`  (Denke daran, das X mit der Zahl zu ersetzen)
    1. Als nächstes wirst du nach deinem Passwort gefragt
1. Wenn du eingeloggt bist, installieren wir die Vogel-Kamera Software
1. Software installieren
    1. Befehl eingeben: `sudo apt-get install -y git python3 python3-dev python3-pip`
    1. Befehl eingeben: `git clone https://github.com/pabera/informatik-ag.git

## Erstes Bild erstellen

1. In den neuen Ordner wechseln
    * `cd informatik-ag`
    * `cd vogelhaus`
1. Abhängigkeiten (*Dependencies*) installieren
    * Script ausführen: `pip install -r requirements.txt`
1. Script ausführen
    * `python3 foto-aufnehmen.py`
1. Um das Foto anzusehen, folgende Befehle ausführen
    1. Startet einen Web-Server auf dem Raspberry Pi
        * `python3 -m http.server -b 80`
    1. Auf eurem Computer, öffnet folgenden Web-Adresse in einem Browser (Denke daran, das X mit der Zahl zu ersetzen)
        * `http://vogelcamX.local/camera.jpg`
