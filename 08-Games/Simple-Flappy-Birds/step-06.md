# Flappy Birds - Schritt 6 - Punkte zählen

1. `punktzahl = 0`:
   Wir erstellen eine Punktzahl und setzen sie am Anfang auf 0.

2. `passierte_roehren = []`:
   Wir machen eine leere Liste, um uns zu merken, welche Röhren wir schon geschafft haben.

3. `schriftart = pygame.font.Font(None, 36)`:
   Wir wählen eine Schriftart aus, um unsere Punkte anzuzeigen.

4. `for i in range(0, len(roehren_liste), 2):`:
   Wir schauen uns jede zweite Röhre an (weil wir immer Paare von oberer und unterer Röhre haben).

5. `roehre = roehren_liste[i]`:
   Wir nehmen eine Röhre aus unserer Liste.

6. `if roehre.right < vogel_x and roehre not in passierte_roehren:`:
   Wir prüfen, ob der Vogel die Röhre geschafft hat und ob wir sie noch nicht gezählt haben.

7. `punktzahl += 1`:
   Wenn der Vogel die Röhre geschafft hat, bekommen wir einen Punkt dazu.

8. `passierte_roehren.append(roehre)`:
   Wir merken uns, dass wir diese Röhre schon gezählt haben.

9. `punktzahl_text = schriftart.render(f"Punkte: {punktzahl}", True, SCHWARZ)`:
   Wir machen aus unserer Punktzahl einen Text, den wir anzeigen können.

10. `bildschirm.blit(punktzahl_text, (10, 10))`:
    Wir zeigen unsere Punktzahl oben links auf dem Bildschirm an.
