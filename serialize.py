import pickle
from mtgsdk import Card
filename = 'eldset'
outfile = open(filename, 'wb')
print('searching')
OriginalEldrainSet = Card.where(set='ELD').all()
print('serializing')
pickle.dump(OriginalEldrainSet,outfile)
outfile.close()