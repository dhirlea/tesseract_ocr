import re
import cv2
import pytesseract
from pytesseract import Output

def main():
    """Take the example of trying to find where a date is in an image. 
    Here our template will be a regular expression pattern that we will match with our OCR results to find the appropriate bounding boxes. 
    We will use the regex module and the image_to_data function for this.
    """
    img = cv2.imread('images/invoice.jpg')
    d = pytesseract.image_to_data(img, output_type=Output.DICT)

    date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 60:
            if re.match(date_pattern, d['text'][i]):
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()