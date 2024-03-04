# Nistkasten mit Kamera

## Vorbereitungen

1.  Wenn nicht bereits geschehen, folge dieser [Anleitung](../01-Kamera-am-Pi/README.md#raspberry-pi-vorbereiten) um deinen Raspberry Pi neu aufzusetzen und dich mit ihm zu verbinden
1. Danach musst du Python installieren und folgendes Repository klonen, [wie hier beschrieben](../01-Kamera-am-Pi/README.md#kamera-software-vorbereiten).

## Video Stream einrichten

1. In den neuen Ordner wechseln
    * `cd informatik-ag`
    * `cd 02-Vogelcam`
1. Abhängigkeiten (*Dependencies*) installieren
    * Script ausführen: `pip install -r requirements.txt`

## Programm automatisch starten

1. Öffne das Terminal auf deinem Raspberry Pi.
1. Gib den folgenden Befehl ein, um die Crontab-Datei zu bearbeiten:

   ```bash
   crontab -e
   ```

1. Wenn du crontab zum ersten Mal verwendest, wird möglicherweise gefragt, welchen Editor du verwenden möchtest. Wähle `nano`, indem du dessen Nummer eingibst und Enter drückst.
1. Scrolle zum Ende der Crontab-Datei und füge folgende Zeile hinzu:

   ```bash
   @reboot python3 /home/meise/informatik-ag/02-Vogelcam/camera.py
   ```

1. Speichere die Datei und verlasse den Editor. Wenn du `nano` verwendest, kannst du dies tun, indem du `Ctrl + X` drückst, dann `Y` zum Bestätigen und `Enter` zum Speichern.
1. Dein Skript sollte jetzt jedes Mal ausgeführt werden, wenn dein Raspberry Pi hochfährt.

## Überprǔfen, ob das Programm läuft

1. Öffne das Terminal auf deinem Raspberry Pi.
1. Gib den folgenden Befehl ein:

   ```bash
   ps aux | grep camera.py
   ```
1. Wenn die Ausgabe einen Eintrag anzeigt, der `informatik-ag` enthält, läuft das Programm. Ansonsten nicht.

## Optional: WLAN Password ändern

```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=DE

network={
    ssid="ESSID"
    psk="Your_wifi_password"
}
```
