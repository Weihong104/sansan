# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:25:39 2024

@author: USER
"""

from PIL import Image

import pytesseract

fileName = "eng.jpg"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open(fileName)

text = pytesseract.image_to_string(img,lang='eng')

print(text.strip())