# Flappy Birds - Schritt 3 - Vogel hinzufügen

1. `SCHWARZ = (0, 0, 0)`:
   Wir mischen die Farbe Schwarz für unseren Vogel.

2. `vogel_x = 50`:
   Wir legen fest, wie weit links unser Vogel sein soll.

3. `vogel_y = HOEHE // 2`:
   Wir setzen unseren Vogel in die Mitte der Höhe des Bildschirms.

4. `vogel_radius = 20`:
   Wir bestimmen, wie groß unser Vogel sein soll.

5. `vogel_geschwindigkeit = 0`:
   Am Anfang bewegt sich unser Vogel noch nicht nach oben oder unten.

6. `schwerkraft = 0.5`:
   Wir legen fest, wie stark die Schwerkraft auf unseren Vogel wirkt.

7. `vogel_geschwindigkeit += schwerkraft`:
   Die Schwerkraft zieht unseren Vogel nach unten.

8. `vogel_y += vogel_geschwindigkeit`:
   Wir bewegen unseren Vogel nach unten, je nachdem wie schnell er fällt.

9. `pygame.draw.circle(bildschirm, SCHWARZ, (int(vogel_x), int(vogel_y)), vogel_radius)`:
   Wir malen unseren Vogel als schwarzen Kreis auf den Bildschirm.
