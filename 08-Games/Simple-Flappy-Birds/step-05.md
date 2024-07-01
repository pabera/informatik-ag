# Flappy Birds - Schritt 5 - Achtung, nicht die Röhren berühren

1. `def pruefe_kollision(roehren):`:
   Wir erstellen eine neue Funktion, die prüft, ob unser Vogel irgendwo anstößt.

2. `vogel_rechteck = pygame.Rect(vogel_x - vogel_radius, vogel_y - vogel_radius, vogel_radius * 2, vogel_radius * 2)`:
   Wir malen ein unsichtbares Quadrat um unseren Vogel, um besser zu erkennen, ob er etwas berührt.

3. `for roehre in roehren:`:
   Wir schauen uns jede Röhre einzeln an.

4. `if vogel_rechteck.colliderect(roehre):`:
   Wir prüfen, ob das Quadrat um unseren Vogel eine Röhre berührt.

5. `return True`:
   Wenn der Vogel eine Röhre berührt, sagen wir "Ja, es gab einen Zusammenstoß".

6. `if vogel_y + vogel_radius > HOEHE or vogel_y - vogel_radius < 0:`:
   Wir prüfen auch, ob der Vogel den oberen oder unteren Rand des Bildschirms berührt.

7. `return False`:
   Wenn der Vogel nichts berührt hat, sagen wir "Nein, kein Zusammenstoß".

8. `if pruefe_kollision(roehren_liste):`:
   Wir rufen unsere neue Funktion auf, um zu prüfen, ob der Vogel etwas berührt hat.

9. `laeuft = False`:
   Wenn der Vogel etwas berührt hat, beenden wir das Spiel.
