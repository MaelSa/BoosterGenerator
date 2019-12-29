import pickle
from mtgsdk import Card
filename = 'ravset'
outfile = open(filename, 'wb')
print('searching')
OriginalEldrainSet = Card.where(set='RAV').all()
print('serializing')
pickle.dump(OriginalEldrainSet,outfile)
outfile.close()