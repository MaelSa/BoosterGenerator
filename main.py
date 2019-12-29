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
    banned_subtypes = ['Forest', 'Mountain', 'Plains', 'Swamp', 'Island', 'Adventure']
    boosterList = []
    rarity_numbers = [0, 0, 0]
    while rarity_numbers != [10, 3, 1]:
        ok_card = False
        card = MtgSet[random.randint(0, len(MtgSet) - 1)]
        if card.subtypes and card.subtypes[0] not in banned_subtypes:
            ok_card, rarity_numbers = okrarity(card, rarity_numbers)
        if ok_card:
            boosterList.append(card)
            MtgSet.remove(card)
    return boosterList


def okrarity(card, rarity_numbers):
    if (card.rarity == 'Rare' or card.rarity == 'Mythic') and rarity_numbers[2] == 0:
        rarity_numbers[2] += 1
        return True, rarity_numbers

    elif card.rarity == 'Uncommon' and rarity_numbers[1] < 3:
        rarity_numbers[1] += 1
        return True, rarity_numbers

    elif card.rarity == 'Common' and rarity_numbers[1] < 10:
        rarity_numbers[0] += 1
        return True, rarity_numbers

    else:
        return False, rarity_numbers


def image_from_url(url):
    rep = urllib.request.urlopen(url).read()
    image = np.asarray(bytearray(rep), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


def transfo_url_to_image(Booster):
    for card in Booster:
        image = image_from_url(card.image_url)
        imgpil = Image.fromarray(image)  # Transformation du tableau en image PIL
        imgpil.save("images/" + card.number + ".jpg")


def placement_images(card_numbers):

    pygame.init()

    # Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((640, 480))
    fenetre.fill((255,255,255))
    # Chargement et collage du fond

    i, j = 0, 0
    print(card_numbers)
    for number in card_numbers:
        print("in for loop")
        visual_pic = pygame.image.load(str(number) + '.jpg').convert()
        print(str(number)+'.jpg')
        fenetre.blit(visual_pic, (i % 3 * 100, j % 3 * 300))

        # Rafraîchissement de l'écran
        pygame.display.flip()

        # BOUCLE INFINIE
    continuer = 1
    while continuer:
        print('infi')
        continuer = int(input())

ourbooster = generateBooster()
print("booster generated")
ourbooster = []
ourbooster.append(MtgSet[57])
#transfo_url_to_image(ourbooster)
print('images generated')
#for card in ourbooster:
#    print(card.name, "rarity : ", card.rarity, 'image : ', card.image_url, 'type : ', card.type)
placement_images([202])