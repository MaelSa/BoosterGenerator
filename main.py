from mtgsdk import Card
import pickle
import random
import copy
# Throne of Edraine code = ELD
# rarity = Rare, Common, Uncommon, Mythic
#
#
infile = open('eldset','rb')
EldrainSet = pickle.load(infile)
infile.close()
print(len(EldrainSet))
lenSet = len(EldrainSet)

def generateBooster():
    banned_subtypes = ['Forest', 'Mountain', 'Plains', 'Swamp', 'Island', 'Adventure']
    boosterList = []
    rarity_numbers = [0, 0, 0]
    while rarity_numbers != [10, 3, 1]:
        ok_card = False
        card = EldrainSet[random.randint(0,len(EldrainSet) -1 )]
        if card.subtypes and card.subtypes[0] not in banned_subtypes:
            ok_card, rarity_numbers = okrarity(card, rarity_numbers)
        if ok_card:
            boosterList.append(card)
            EldrainSet.remove(card)
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

ourbooster = generateBooster()
for card in ourbooster:
    print(card.name, "rarity : ", card.rarity, 'image : ', card.image_url, 'type : ', card.type)