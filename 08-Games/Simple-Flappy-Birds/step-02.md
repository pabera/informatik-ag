# Flappy Birds - Schritt 2 - Röhren hinzufügen

1. `import random`:
   Wir holen uns eine Zufallskiste, um später zufällige Zahlen zu erzeugen.

2. `GRUEN = (0, 255, 0)`:
   Wir mischen die Farbe Grün für unsere Röhren.

3. `roehren_breite = 50`:
   Wir legen fest, wie breit unsere Röhren sein sollen.

4. `roehren_abstand = 200`:
   Wir bestimmen, wie groß der Abstand zwischen den oberen und unteren Röhren sein soll.

5. `roehren_x = BREITE`:
   Wir sagen, dass die Röhren am rechten Rand des Bildschirms starten sollen.

6. `roehren_geschwindigkeit = 3`:
   Wir legen fest, wie schnell sich die Röhren bewegen sollen.

7. `roehren_liste = []`:
   Wir erstellen eine leere Liste, in die wir später unsere Röhren packen.

8. `def erstelle_roehre():`:
   Hier basteln wir eine Funktion, die neue Röhren für uns macht.

9. `roehren_hoehe = random.randint(100, HOEHE - 100 - roehren_abstand)`:
   Wir wählen zufällig aus, wie hoch die Lücke zwischen den Röhren sein soll.

10. `untere_roehre = pygame.Rect(...)` und `obere_roehre = pygame.Rect(...)`:
    Wir zeichnen unsichtbare Rechtecke für die obere und untere Röhre.

11. `def zeichne_roehren(roehren):`:
    Diese Funktion malt alle unsere Röhren grün an.

12. `def bewege_roehren(roehren):`:
    Diese Funktion lässt die Röhren von rechts nach links fliegen.

13. `if len(roehren_liste) == 0 or roehren_liste[-1].right < BREITE - 200:`:
    Wenn keine Röhren da sind oder die letzte Röhre weit genug links ist, machen wir neue.

14. `roehren_liste.extend(erstelle_roehre())`:
    Wir fügen neue Röhren zu unserer Liste hinzu.

15. `roehren_liste = bewege_roehren(roehren_liste)`:
    Wir bewegen alle Röhren ein Stückchen nach links.

16. `zeichne_roehren(roehren_liste)`:
    Wir malen alle Röhren auf den Bildschirm.
