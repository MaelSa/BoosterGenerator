from mtgsdk import Card
import pickle
import random
import random
import urllib.request
import cv2
import numpy as np
import os
import pygame
from pygame.locals import *
from PIL import Image
import copy
# Throne of Edraine code = ELD
# rarity = Rare, Common, Uncommon, Mythic
#
#
infile = open('ravset','rb')
MtgSet = pickle.load(infile)
infile.close()
print(len(MtgSet))
lenSet = len(MtgSet)

def generateBooster():
    MtgSetBooster = copy.copy(MtgSet)
    banned_subtypes = ['Forest', 'Mountain', 'Plains', 'Swamp', 'Island', 'Adventure']
    boosterList = []
    rarity_numbers = [0, 0, 0]
    while rarity_numbers != [9, 4, 2]:
        ok_card = False
        card = MtgSetBooster[random.randint(0, len(MtgSetBooster) - 1)]
        if card.subtypes and card.subtypes[0] not in banned_subtypes:
            ok_card, rarity_numbers = okrarity(card, rarity_numbers)
        if ok_card:
            boosterList.append(card)
            MtgSetBooster.remove(card)
    return boosterList


def okrarity(card, rarity_numbers):
    if (card.rarity == 'Rare' or card.rarity == 'Mythic') and rarity_numbers[2] < 2:
        rarity_numbers[2] += 1
        return True, rarity_numbers

    elif card.rarity == 'Uncommon' and rarity_numbers[1] < 4:
        rarity_numbers[1] += 1
        return True, rarity_numbers

    elif card.rarity == 'Common' and rarity_numbers[1] < 9:
        rarity_numbers[0] += 1
        return True, rarity_numbers

    else:
        return False, rarity_numbers


def placement_images(card_numbers):

    pygame.init()

    # Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((2481, 3510))
    fenetre.fill((255,255,255))
    # Chargement et collage du fond

    print(len(card_numbers))
    for sheet in range(10):
        for c in range(9):
            visual_pic = pygame.image.load('images/' + str(card_numbers[0]) + '.jpg').convert()
            card_numbers.remove(card_numbers[0])
            visual_pic = pygame.transform.scale(visual_pic, (744, 1040))
            fenetre.blit(visual_pic, ((c%3)*784 + 50, (c//3)*1070 + 50))

            # Rafraîchissement de l'écran
            pygame.display.flip()

        # BOUCLE INFINIE
        pygame.image.save(fenetre, f"screenshot{sheet}.jpg")
    continuer = 1
    while continuer:
        continuer = int(input())
card_numbers_tot = []
for i in range(6):

    ourbooster = generateBooster()
    card_numbers_booster = [card.number for card in ourbooster]
    card_numbers_tot += card_numbers_booster
print(card_numbers_tot)
print("booster generated")
#for card in ourbooster:
#    print(card.name, "rarity : ", card.rarity, 'image : ', card.image_url, 'type : ', card.type)
placement_images(card_numbers_tot)