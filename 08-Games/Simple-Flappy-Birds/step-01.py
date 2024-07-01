import pygame

# Pygame initialisieren
pygame.init()

# Spielfenster einrichten
BREITE = 400
HOEHE = 600
bildschirm = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption("Flappy Vogel")

# Farben
WEISS = (255, 255, 255)

# Spielschleife
uhr = pygame.time.Clock()
laeuft = True

while laeuft:
    for ereignis in pygame.event.get():
        if ereignis.type == pygame.QUIT:
            laeuft = False
    # Alles zeichnen
    bildschirm.fill(WEISS)

    pygame.display.flip()
    uhr.tick(60)

pygame.quit()
