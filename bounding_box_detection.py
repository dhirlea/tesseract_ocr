import cv2
import re
import pytesseract
from pytesseract import Output


def load_image(img_path, config):
    image = cv2.imread(img_path)
    image_data = pytesseract.image_to_data(image, output_type=Output.DICT, config=config)
    return image, image_data

def plot_image_with_boxes(image, image_data):
    n_boxes = len(image_data['text'])
    for i in range(n_boxes):
        if int(float(image_data['conf'][i])) > 60:
            (x, y, w, h) = (image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i])
            img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Image', img)
    cv2.waitKey(0)

def image_to_txt(image_data, file_path):
    alphanumeric = u'[a-zA-Z0-9]+'
    document_text = [sequence for sequence in image_data['text'] if re.search(alphanumeric, sequence)]
    with open(file_path,'w', encoding='utf-8') as f:
        for sequence in document_text:
            f.write(sequence + '\n')

def main():

    img_path = 'images/invoice.jpg'
    file_path = 'output_text_files/invoice.txt'
    custom_config = r'--oem 3 --psm 3'

    img, image_data = load_image(img_path, custom_config)
    image_to_txt(image_data, file_path)
    plot_image_with_boxes(img, image_data)

if __name__ =='__main__':
    main()