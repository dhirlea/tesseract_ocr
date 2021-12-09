
import cv2 
import pytesseract

def convert_img_to_txt(image, configuration = None):
    """ Utility function to convert custom image into text file
    """
    converted_image = pytesseract.image_to_string(image, config=configuration)
    return converted_image

def main():
    img = cv2.imread('test_eng.png')
    custom_config = r'--oem 3 --psm 3' #oem argument defines the OCR engine mode, and psm argument specifies the image segmentation mode. See https://nanonets.com/blog/ocr-with-tesseract/
    with open('test_eng.txt', 'w', encoding='utf-8') as f:
        f.write(convert_img_to_txt(img, custom_config))
     
if __name__ =='__main__':
    main()