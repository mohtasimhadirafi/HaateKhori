import cv2
import pytesseract
import numpy as np

IMG_DIR = 'images/'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def pre_processing(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # converting it to binary image
    threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # saving image to view threshold image
    cv2.imwrite('thresholded.png', threshold_img)

    # cv2.imshow('threshold image', threshold_img)
    # Maintain output window until
    # user presses a key
    # cv2.waitKey(0)
    # Destroying present windows on screen
    # cv2.destroyAllWindows()

    return threshold_img


def parse_text(threshold_img):
    # configuring parameters for tesseract
    tesseract_config = r'--oem 3 --psm 10'
    # now feeding image to tesseract
    details = pytesseract.image_to_string(threshold_img,
                                          config=tesseract_config, lang='eng')
    return details


if __name__ == "__main__":
    image = cv2.imread(IMG_DIR + 'D.png')

    thresholds_image = pre_processing(image)
    parsed_data = parse_text(thresholds_image)
    parsed_data = parsed_data[0]
    print(parsed_data)


