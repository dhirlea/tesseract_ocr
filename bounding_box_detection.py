import cv2
import re
import pytesseract
from pytesseract import Output

def main():

    img = cv2.imread('images/invoice.jpg')
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    alphanumeric = u'[a-zA-Z0-9]+'
    document_text = [sequence for sequence in d['text'] if re.search(alphanumeric, sequence)]
    with open('output_text_files/receipt.txt','w') as f:
        for sequence in document_text:
            f.write(sequence + '\n')
    cv2.imshow('img', img)
    cv2.waitKey(0)

if __name__ =='__main__':
    main()