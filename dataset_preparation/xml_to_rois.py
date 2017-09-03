# -*- coding: iso-8859-1 -*-
from shutil import copy2
import shutil
import os
import xml.etree.ElementTree
import cv2

path = '/Volumes/WD/logodata'
ext = '.jpg'
dstext = '.jpg'
postfix = '_det'

skip_occluded = True

fuse_occluded = True

outpath = os.path.join(path, '..', 'processed', 'data')

annotationspath = os.path.join(outpath, 'Annotations')
imagespath = os.path.join(outpath, 'Images')
imagesetspath = os.path.join(outpath, 'ImageSets')
brandspath = os.path.join(outpath, 'brands')

if os.path.exists(outpath):
    shutil.rmtree(outpath)

os.makedirs(annotationspath)
os.makedirs(imagespath)
os.makedirs(imagesetspath)

imglist = ''
brandlist = list()
subdirID = 0
dirs = None
for r, subdirs, files in os.walk(path):
    if dirs == None:
        dirs = subdirs
    #parent = dirs[subdirID]
    subdirID += 1
    for filename in files:
        if not filename.endswith('.xml'):
            continue

        filewithpath = os.path.join(r, filename)
        parent = filewithpath.split('/')[-2]
        parser = xml.etree.ElementTree.XMLParser(encoding="utf-8")
        root = xml.etree.ElementTree.parse(filewithpath, parser = parser).getroot()

        imagename = filename.split('.')[0]

        imglist += parent + '_' + imagename + postfix + '\n'

        #with open(os.path.join(annotationspath, parent + "_" + imagename + postfix + dstext + '.bboxes.txt'), 'w') as annotfile:
        im = cv2.imread(os.path.join(r, imagename + ext))
        print(os.path.join(r, imagename + ext))
        i = 0
        for obj in root.findall('object'):
            brand = obj.find('name').text.encode('utf-8').lower()
            if brand == "1fcköln":
                brand = "fckoeln"
            if brand == "aluratek":
                brand = "aluratek-symbol"
            if brand == "apecase":
                brand = "apecase-symbol"
            if brand == "apecase-teilsichtbar":
                brand = "apecase-symbol-teilsichtbar"
            if brand == "armitron1":
                brand = "armitron"
            if brand == "audi":
                brand = "audi-symbol"
            if brand == "b":
                brand = "bridgestone"
            if brand == "basf-symbol":
                brand = "basf"
            if "bertha1" in brand:
                brand = brand.replace("bertha1", "bertha")
            if "boing" in brand:
                brand = brand.replace("boing", "boeing")
            if "budweiser1" in brand:
                brand = brand.replace("budweiser1", "budweiser")
            if "budweiser2" in brand:
                brand = brand.replace("budweiser2", "budweiser")
            if brand == "budweiser-b":
                brand = "budweiser-b-symbol"
            if brand == "budweiser-teilsichtbar":
                brand = "budweiser-symbol-teilsichtbar"
            if "bundweiser" in brand:
                brand = brand.replace("bundweiser", "budweiser")
            if brand == "burgerking":
                brand = "burgerking-symbol"
            if brand == "burgerking-teilsichtbar":
                brand = "burgerking-symbol-teilsichtbar"
            if "canon1" in brand:
                brand = brand.replace("canon1", "canon")
            if "canon2" in brand:
                brand = brand.replace("canon2", "canon")
            if "cartier1" in brand:
                brand = brand.replace("cartier1", "cartier")
            if "caterpillar1" in brand:
                brand = brand.replace("caterpillar1", "caterpillar")
            if brand == "chevrolet1":
                brand = brand.replace("chevrolet1", "chevrolet")
            if brand == "citroen":
                brand == "citroen-symbol"
            if brand == "colgate1":
                brand = "colgate"
            if "dadone" in brand:
                brand = brand.replace("dadone", "danone")
            if brand == "cvs-symbol" or brand == "cvs-logo":
                brand = "cvspharmacy"
            if brand == "danone1":
                brand = "danone"
            if "fils" in brand:
                brand = brand.replace("fils", "fila")
            if brand == "google":
                brand = "google-symbol"
            if brand == "gucci1":
                brand = "gucci"
            if brand == "gucci logo":
                brand = "gucci-symbol"
            if "heineke" in brand:
                brand = brand.replace("heineke", "heineken")
            if brand == "hersheys1":
                brand = "hersheys"
            if brand == "hungry jacks logo":
                brand = "hungry jacks-symbol"
            if "hyundri" in brand:
                brand = brand.replace("hyundri", "hyundai")
            if "kellogg`s-k" in brand:
                brand = brand.replace("kellogg`s-k", "kellogg`s-symbol")
            if "kia-logo" in brand:
                brand = brand.replace("kia-logo", "kia")
            if brand == "lego":
                brand = "lego-symbol"
            if brand == "lego-teilsichtbar":
                brand = "lego-symbol-teilsichtbar"
            if "louis vuitton2" in brand:
                brand = brand.replace("louis vuitton2", "louisvuitton")
            if brand == "mastercard1":
                brand = "mastercard"
            if brand == "mcdonalds":
                brand = "mcdonalds-symbol"
            if brand == "mcdonalds-teilsichtbar":
                brand = "mcdonalds-symbol-teilsichtbar"
            if brand == "mercedes" or brand == "mercedes-logo":
                brand = "mercedesbenz-symbol"
            if brand == "mercedes-schrift" or brand == "mercedes-schriftzug":
                brand = "mercedesbenz"
            if brand == "mercedes-teilsichtbar":
                brand = "mercedesbenz-symbol-teilsichtbar"
            if brand == "nestle1" or brand == "nestle2":
                brand = "nestle"
            if brand == "nike":
                brand = "nike-symbol"
            if "nikelogo" in brand:
                brand = brand.replace("nikelogo", "nike")
            if brand == "lego1":
                brand = "lego"
            if brand == "nivea1":
                brand = "nivea"
            if brand == "olympia":
                brand = "olympicgames"
            if brand == "pizzahut-logo":
                brand = "pizzahut"
            if "ruffels" in brand:
                brand = brand.replace("ruffels", "ruffles")
            if brand == "the home depot1" or brand == "the home depot-logo":
                brand = "thehomedepot"
            if "vl" in brand:
                brand = brand.replace("vl", "louisvuitton")
            if brand == "volksbank":
                brand = "volksbank-symbol"
            if brand == "ströker":
                brand = "stroeer"
            if brand == "görtz":
                brand = "goertz"
            if "schriftzug" in brand:
                brand = brand.replace("-schriftzug", "")
            if "schrift" in brand:
                brand = brand.replace("-schrift", "")
            if "teilsichtbar" in brand:
                brand = brand.replace(u"-teilsichtbar", "")
                obj.find('truncated').text = str(1)
            if "logo" in brand:
                brand = brand.replace('logo', 'symbol')
            if "`" in brand:
                brand = brand.replace("`", "")
            if "." in brand:
                brand = brand.replace(".", "")
            brand = brand.replace(" ", "")

            if brand == "chanel":
                brand = "chanel-text"
            if brand == "chanel-symbol":
                brand = "chanel"

            if brand == "citroen":
                brand = "citroen-text"
            if brand == "citroen-symbol":
                brand = "citroen"

            if brand == "mcdonalds":
                brand = "mcdonalds-text"
            if brand == "mcdonalds-symbol":
                brand = "mcdonalds"

            if brand == "mercedesbenz":
                brand = "mercedes-text"
            if brand == "mercedesbenz-symbol":
                brand = "mercedes"

            if brand == "nike-symbol":
                brand = "nike"

            if brand == "porsche":
                brand = "porsche-text"
            if brand == "porsche-symbol":
                brand = "porsche"

            if brand == "unicef-symbol":
                brand = "unicef"

            if brand == "vodafone-symbol":
                brand = "vodafone"

            #if brand == u"ströker":
            #    brand = "stroeker"

            bndbox = obj.find('bndbox')
            x1 = int(bndbox[0].text)
            y1 = int(bndbox[1].text)
            x2 = int(bndbox[2].text)
            y2 = int(bndbox[3].text)

            brandlist.append(brand)
            roi = im[y1:y2, x1:x2]
            folder = os.path.join(brandspath, brand)
            if not os.path.exists(folder):
                os.makedirs(folder)
            cv2.imwrite(os.path.join(folder, parent + "_" +imagename + '_' + str(i) + '.jpg'), roi)

            #annotfile.write(str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + brand + '\n')
            i += 1

        #copy2(os.path.join(r, imagename + ext), os.path.join(imagespath, parent + '_' + imagename + postfix + dstext))

with open(os.path.join(imagesetspath, 'ownlogos' + postfix + '.txt'), 'w') as f:
    f.write(imglist)

with open(os.path.join(outpath, 'brands.txt'), 'w') as f:
    for brand in set(brandlist):
        f.write(brand + '\n')