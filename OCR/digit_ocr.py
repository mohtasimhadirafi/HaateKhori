import pytesseract

import cv2

IMG_DIR = 'images/'
img = cv2.imread(IMG_DIR + 'A.png')
text = pytesseract.image_to_string(img, lang='eng',
                                   config='--dpi 300 --psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')

print(text[0])
