# Flappy Birds in Scratch

Das Programmieren von "Flappy Bird" in Scratch ist ein großartiges Projekt, um Programmierkenntnisse spielerisch zu erweitern! Hier ist eine schrittweise Anleitung, um eine einfache Version von "Flappy Bird" in Scratch zu erstellen:

## Schritt 1: Einrichten des Scratch-Projekts

1. Öffne Scratch: Gehe auf die Scratch-Website (https://scratch.mit.edu) und starte ein neues Projekt.
2. Lösche die Katze: Entferne die Standard-Sprite durch Rechtsklick und Auswahl von "Löschen".

## Schritt 2: Erstelle den Flappy Bird Sprite

1. Neuen Sprite hinzufügen: Klicke auf das Symbol „Sprite wählen“ und wähle einen Vogel oder ein anderes Objekt, das du als Spieler verwenden möchtest.
2. Größe anpassen: Stelle die Größe des Sprites so ein, dass es gut ins Spiel passt, typischerweise zwischen 10% und 20%.

## Schritt 3: Programmieren der Vogelbewegung

1. Bewegungscode hinzufügen: Klicke auf deinen Vogel-Sprite und füge folgenden Code im Bereich „Code“ hinzu:

    ```scratch
    Wenn grüne Flagge angeklickt
    gehe zu x: 0 y: 0
    wiederhole fortlaufend
        wenn Taste (Leertaste) angeklickt
        ändere y um 10
        warte 0.3 Sekunden
        ändere y um -2
    ```

    Dies lässt den Vogel fliegen, wenn die Leertaste gedrückt wird, und lässt ihn sonst fallen.

## Schritt 4: Erstellen der Röhren (Hindernisse)

1. Neues Sprite für Röhren: Klicke auf „Sprite wählen“ und suche nach einem Röhren-Sprite oder zeichne eine Röhre im Kostümeditor.
2. Röhrenbewegungscode hinzufügen: Füge diesem Sprite folgenden Code hinzu:

    ```scratch
    Wenn grüne Flagge angeklickt
    setze x auf 240
    wiederhole fortlaufend
        gehe x: -5 y: 0
        warte 0.05 Sekunden
        wenn x < -240 dann
            setze x auf 240
            setze y auf zufällige Zahl zwischen -100 und 100
    ```

    Dies wird die Röhren kontinuierlich von rechts nach links bewegen und sie zufällig neu positionieren.

## Schritt 5: Hinzufügen von Spiellogik

1. Kollisionserkennung: Füge dem Vogel-Sprite Code hinzu, um das Spiel zu beenden, wenn der Vogel eine Röhre berührt:

    ```scratch
    wenn ich Röhre berühre dann
    sende [Spielende v]
    stoppe [alle v]
    ```

2. Punktezählung: Du kannst eine Punktevariable hinzufügen, die erhöht wird, jedes Mal wenn der Vogel eine Röhre passiert.

## Schritt 6: Verfeinern und Testen

- Teste dein Spiel gründlich, um sicherzustellen, dass alles wie erwartet funktioniert.
- Füge Sounds und Musik hinzu für eine ansprechendere Spielerfahrung.
- Passe das Aussehen der Sprites und des Hintergrunds an, um dein Spiel visuell attraktiver zu machen.
