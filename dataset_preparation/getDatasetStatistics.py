# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:17:58 2017

@author: herrma
"""

#import os
import xmltodict
import numpy as np
from dirRecursive import dirRecursive

path = '~/LogoData-cleaned/voc_format'
xmlFiles = dirRecursive(path, '*.xml')

print('Annotated images: {:d}'.format(len(xmlFiles)))

nBoxes = 0
maxBoxes = 0
boxesList = []
brands = {}
fullBrandList = np.empty(0,dtype='S')
for xmlPath in xmlFiles:        
    ### read ground truth bounding boxes
    with open(xmlPath) as fx:
        annot = xmltodict.parse(fx.read())
        
    # get object list
    objects = annot['annotation']['object']    
    if not isinstance(objects, list):
        objects = [objects]
    
    # number of annotated objects
    nBoxes += len(objects)
    if len(objects) > maxBoxes:
        maxBoxes = len(objects)
    boxesList.append(len(objects))
    
    # collect classes of annotated objects
    subPath = '/'.join(xmlPath.split('\\')[-2:])
    for obj in objects:
        if obj['name'] in brands:
            brands[obj['name']][subPath] = 1
        else:
            brands[obj['name']] = {subPath:1}
        fullBrandList = np.append(fullBrandList, obj['name'])
            
sortedBrands = [(key, brands[key]) for key in sorted(brands)]

# frequency analysis and backreferences
brand,freq = np.unique(fullBrandList, return_counts=True)
# sort by frequency
idx = np.argsort(-freq)
brandFreq = [(brand[i],freq[i]) for i in idx]
# sort by name 
brandLow = np.core.defchararray.lower(brand)
idx = np.argsort(brandLow)
brandName = [(brandLow[i],freq[i]) for i in idx]

# some lists for manual inspection and reference
uniqueBrands = np.unique(np.array([s.split('-')[0] for s in brandLow]))
uniqueSpecifiers = np.unique(np.array(['-'.join(s.split('-')[1:]) if len(s.split('-')) > 1 else 'none' for s in brandLow]))

# file output
np.savetxt('brandFreq.csv', freq, fmt='%d')
np.savetxt('boxesPerImage.csv', np.asarray(boxesList), fmt='%d')

# print stats
print('Different brands: {:d}'.format(brand.size))
print('Annotated logos: {:d}'.format(nBoxes))
print('Maximum logos in one image: {:d}'.format(maxBoxes))
                    
        
            