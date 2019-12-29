from mtgsdk import Card

import random

# Throne of Edraine code = ELD
# rarity = Rare, Common, Uncommon, Mythic
#
#
OriginalEldrainSet = Card.where(set='ELD').all()
print(OriginalEldrainSet)