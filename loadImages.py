import pickle
from mtgsdk import Card
infile = open('ravset','rb')
MtgSet = pickle.load(infile)
infile.close()
import urllib.request
import cv2
from PIL import Image
import numpy as np

def image_from_url(url):
    rep = urllib.request.urlopen(url).read()
    image = np.asarray(bytearray(rep), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    return image


def transfo_url_to_image(Booster):
    print(f'{len(Booster)} images to load')
    loaded_images = 0
    for card in Booster:
        loaded_images += 1
        print(loaded_images)
        image = image_from_url(card.image_url)
        imgpil = Image.fromarray(image)  # Transformation du tableau en image PIL
        imgpil.save("images/" + card.number + ".jpg")

transfo_url_to_image(MtgSet)

# Import requests, shutil python module.
import requests
import shutil
def download_image_2(MtgSet):
    for card in MtgSet:
        print(card.number)
        image_url = card.image_url
        resp = requests.get(image_url, stream=True)
        local_file = open(f'images/{card.number}.jpg', 'wb')
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)
        del resp

#download_image_2(MtgSet)
