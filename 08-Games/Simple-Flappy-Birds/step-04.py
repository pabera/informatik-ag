import pygame
import random

# Pygame initialisieren
pygame.init()

# Spielfenster einrichten
BREITE = 400
HOEHE = 600
bildschirm = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption("Flappy Bird")

# Farben
WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)
GRUEN = (0, 255, 0)

# Vogel-Eigenschaften
vogel_x = 50
vogel_y = HOEHE // 2
vogel_radius = 20
vogel_geschwindigkeit = 0
schwerkraft = 0.5
sprung_staerke = -10

# Roehren-Eigenschaften
roehren_breite = 50
roehren_abstand = 200
roehren_x = BREITE
roehren_geschwindigkeit = 3
roehren_liste = []

# Spielschleife
uhr = pygame.time.Clock()
laeuft = True

def erstelle_roehre():
    roehren_hoehe = random.randint(100, HOEHE - 100 - roehren_abstand)
    untere_roehre = pygame.Rect(roehren_x, roehren_hoehe + roehren_abstand, roehren_breite, HOEHE - roehren_hoehe - roehren_abstand)
    obere_roehre = pygame.Rect(roehren_x, 0, roehren_breite, roehren_hoehe)
    return untere_roehre, obere_roehre

def zeichne_roehren(roehren):
    for roehre in roehren:
        pygame.draw.rect(bildschirm, GRUEN, roehre)

def bewege_roehren(roehren):
    for roehre in roehren:
        roehre.x -= roehren_geschwindigkeit
    return [roehre for roehre in roehren if roehre.right > 0]

while laeuft:
    for ereignis in pygame.event.get():
        if ereignis.type == pygame.QUIT:
            laeuft = False
        if ereignis.type == pygame.KEYDOWN:
            if ereignis.key == pygame.K_SPACE:
                vogel_geschwindigkeit = sprung_staerke

    # Vogel-Position aktualisieren
    vogel_geschwindigkeit += schwerkraft
    vogel_y += vogel_geschwindigkeit

    # Roehren erstellen und bewegen
    if len(roehren_liste) == 0 or roehren_liste[-1].right < BREITE - 200:
        roehren_liste.extend(erstelle_roehre())
    roehren_liste = bewege_roehren(roehren_liste)

    # Alles zeichnen
    bildschirm.fill(WEISS)
    pygame.draw.circle(bildschirm, SCHWARZ, (int(vogel_x), int(vogel_y)), vogel_radius)
    zeichne_roehren(roehren_liste)

    pygame.display.flip()
    uhr.tick(60)

pygame.quit()
