# Flappy Birds - Schritt 1 - Spielfeld erstellen

1. `import pygame`:
   Hier holen wir uns die Pygame-Werkzeugkiste, die wir für unser Spiel brauchen.

2. `pygame.init()`:
   Wir sagen Pygame "Mach dich bereit, wir wollen ein Spiel machen!"

3. `BREITE = 400` und `HOEHE = 600`:
   Wir bestimmen, wie groß unser Spielfenster sein soll.

4. `bildschirm = pygame.display.set_mode((BREITE, HOEHE))`:
   Hier erschaffen wir unser Spielfenster mit der festgelegten Größe.

5. `pygame.display.set_caption("Flappy Vogel")`:
   Wir geben unserem Spiel einen Namen, der oben im Fenster erscheint.

6. `WEISS = (255, 255, 255)`:
   Wir mischen die Farbe Weiß, indem wir Rot, Grün und Blau mischen.

7. `uhr = pygame.time.Clock()`:
   Wir holen uns eine Uhr, um zu bestimmen, wie schnell unser Spiel läuft.

8. `laeuft = True`:
   Wir sagen, dass unser Spiel jetzt anfängt zu laufen.

9. `while laeuft:`:
   Solange unser Spiel läuft, machen wir immer wieder Folgendes:

10. `for ereignis in pygame.event.get():`:
    Wir schauen, ob der Spieler etwas gemacht hat (z.B. eine Taste gedrückt).

11. `if ereignis.type == pygame.QUIT:`:
    Wenn der Spieler das Spiel beenden will...

12. `laeuft = False`:
    ...dann sagen wir, dass das Spiel nicht mehr laufen soll.

13. `bildschirm.fill(WEISS)`:
    Wir malen den ganzen Bildschirm weiß an.

14. `pygame.display.flip()`:
    Wir zeigen alles, was wir gemalt haben, auf dem Bildschirm.

15. `uhr.tick(60)`:
    Wir sagen unserer Uhr, dass sie 60 Mal pro Sekunde ticken soll.

16. `pygame.quit()`:
    Wenn das Spiel vorbei ist, räumen wir alles ordentlich auf.
