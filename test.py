import pygame
import os
pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))
fenetre.fill((255,255,255))
# Chargement et collage du fond

i, j = 0, 0
for pic in os.listdir('images'):
    print(pic)
    visual_pic = pygame.image.load(str(pic)).convert()
    fenetre.blit(visual_pic, (i % 3 * 100, j % 3 * 300))

# Rafraîchissement de l'écran
pygame.display.flip()

    # BOUCLE INFINIE
continuer = 1
while continuer:
    print('infi')
    continuer = int(input())