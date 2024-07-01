# Flappy Birds - Schritt 4 - Vogel springen lassen

1. `sprung_staerke = -10`:
   Wir legen fest, wie stark unser Vogel nach oben springen kann. Die negative Zahl bedeutet, dass er nach oben fliegt.

2. `if ereignis.type == pygame.KEYDOWN:`:
   Wir prüfen, ob eine Taste gedrückt wurde.

3. `if ereignis.key == pygame.K_SPACE:`:
   Wir schauen, ob die Leertaste gedrückt wurde.

4. `vogel_geschwindigkeit = sprung_staerke`:
   Wenn die Leertaste gedrückt wurde, lassen wir den Vogel nach oben springen.
