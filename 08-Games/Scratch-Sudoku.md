# Sudoku in Scratch

Sudoku in Scratch zu programmieren ist eine großartige Möglichkeit, um logisches Denken und Programmierkenntnisse zu entwickeln. Hier ist eine schrittweise Anleitung, um ein einfaches Sudoku-Spiel zu erstellen, bei dem zu Beginn einige Zellen gemäß den Sudoku-Regeln vorbefüllt sind.

## Schritt 1: Einrichten des Scratch-Projekts

1. Öffne Scratch: Gehe auf die Scratch-Website (https://scratch.mit.edu) und starte ein neues Projekt.
2. Lösche die Katze: Entferne das Standard-Sprite, indem du es mit der rechten Maustaste anklickst und "Löschen" auswählst.

## Schritt 2: Erstelle das Spielfeld

1. Neuen Sprite für das Gitter erstellen: Erstelle ein neues Sprite, das das Sudoku-Gitter darstellt. Du kannst dies im Kostümeditor zeichnen. Ein typisches Sudoku-Gitter hat 9x9 Felder, die in 3x3-Blöcke unterteilt sind.
2. Positioniere das Gitter: Zentriere das Gitter auf dem Bildschirm.

## Schritt 3: Erstelle die Zellen

1. Neue Sprites für Zellen: Erstelle für jede Zelle ein eigenes Sprite oder verwende Klone. Jedes dieser Sprites repräsentiert eine Zelle im Sudoku-Gitter.
2. Positioniere die Zellen: Platziere jede Zelle entsprechend ihrer Position im Gitter.
3. Füge Variablen hinzu: Jedes Zell-Sprite benötigt eine Variable, die seinen Wert speichert (0 für leere Zellen).

## Schritt 4: Initialisiere das Spielbrett

1. Sudoku-Logik einführen: Beim Start des Spiels sollten einige Zellen gemäß den Sudoku-Regeln vorbefüllt sein. Hierfür brauchst du eine Liste oder mehrere Listen, die vordefinierte gültige Zahlen enthalten.
2. Skript zum Befüllen der Zellen:

    ```scratch
    Wenn grüne Flagge angeklickt
    für jede [Zelle v] aus [Liste der Zellen v]
        setze [Wert v] von [Zelle v] auf [vorbefüllte Zahl aus Liste]
    ```

## Schritt 5: Eingabe der Zahlen durch den Spieler

1. Interaktion ermöglichen: Ermögliche dem Spieler, Zahlen einzugeben, indem er auf eine Zelle klickt und eine Zahl auf der Tastatur tippt.
2. Prüfe die Eingaben: Stelle sicher, dass die Spieler keine ungültigen Zahlen in eine Zelle eingeben können.

    ```scratch
    Wenn [diese Zelle v] angeklickt
    frage [Gib eine Zahl ein (1-9)] und warte
    wenn <Antwort ist eine gültige Zahl> dann
        setze [Wert v] von [dieser Zelle v] auf [Antwort]
    ```

## Schritt 6: Implementiere Spiellogik

1. Überprüfe das Brett: Füge Logik hinzu, um zu prüfen, ob das Spiel gewonnen wurde, d.h. alle Zellen sind korrekt ausgefüllt.
2. Fehlererkennung: Füge eine Prüfung hinzu, um festzustellen, ob sich irgendwo Fehler im Gitter befinden.

## Schritt 7: Verfeinern und Testen

- Teste dein Spiel: Spiele mehrere Runden, um sicherzustellen, dass alles funktioniert.
- Füge visuelle und akustische Effekte hinzu: Verbessere die Spielerfahrung durch ansprechende Grafiken und Soundeffekte.
