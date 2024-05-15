from PIL import Image
import keyboard as kb
import cv2
import pytesseract as pytess
import pyscreenshot


def on_press():
    # prints coins in inventory
    if kb.is_pressed('ctrl+shift+down'):
        im_b_gold = pyscreenshot.grab(bbox=(1755,890,1785,920))
        im_b_silver = pyscreenshot.grab(bbox=(1795,890,1825,920))
        im_b_copper = pyscreenshot.grab(bbox=(1833,880,1853,935))

        # im_b_copper.show()

        im_b_gold.save('C:/Users/alven/OneDrive/Bilder/Img_grab_test/im_b_gold.png')
        im_b_silver.save('C:/Users/alven/OneDrive/Bilder/Img_grab_test/im_b_silver.png')
        im_b_copper.save('C:/Users/alven/OneDrive/Bilder/Img_grab_test/im_b_copper.png')
    
        im_b_gold = cv2.imread('C:/Users/alven/OneDrive/Bilder/Img_grab_test/im_b_gold.png')
        im_b_silver = cv2.imread('C:/Users/alven/OneDrive/Bilder/Img_grab_test/im_b_silver.png')
        im_b_copper = cv2.imread('C:/Users/alven/OneDrive/Bilder/Img_grab_test/im_b_copper.png')

        gray_g = cv2.cvtColor(im_b_gold, cv2.COLOR_BGR2GRAY)
        gray_s = cv2.cvtColor(im_b_silver, cv2.COLOR_BGR2GRAY)
        gray_c = cv2.cvtColor(im_b_copper, cv2.COLOR_BGR2GRAY)

        noise_g = cv2.fastNlMeansDenoising(gray_g, None, 10, 7, 21)
        noise_s = cv2.fastNlMeansDenoising(gray_s, None, 10, 7, 21)
        noise_c = cv2.fastNlMeansDenoising(gray_c, None, 10, 7, 21)

        pytess.pytesseract.tesseract_cmd = "C:/Users/alven/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

        text_gold = pytess.image_to_string(noise_g)
        text_silver = pytess.image_to_string(noise_s)
        text_copper = pytess.image_to_string(noise_c)
        
        text_gold = text_gold.replace("\n", "")
        text_silver = text_silver.replace("\n", "")
        text_copper = text_copper.replace("\n", "")

        int_gold = int(text_gold)
        int_silver = int(text_silver)
        int_copper = int(text_copper)

        if int_silver < 10:
            text_silver = "0" + text_silver
        if int_copper < 10:
            text_copper = "0" + text_copper

        text_coints = f"{text_gold}{text_silver}{text_copper}"

        with open('C:/Users/alven/OneDrive/Bilder/Img_grab_test/coins.txt', 'a') as f:
            f.write(f"{text_coints}\n")
  
        return False

    # prints fish caught
    if kb.is_pressed('ctrl+shift+up'):
        im_f=pyscreenshot.grab(bbox=(440,310,780,400))

        im_f.save('C:/Users/alven/OneDrive/Bilder/Img_grab_test/im_f.png')
    
        img_f = Image.open('C:/Users/alven/OneDrive/Bilder/Img_grab_test/im_f.png')

        pytess.pytesseract.tesseract_cmd = "C:/Users/alven/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

        text = pytess.image_to_string(img_f)

        print(text)


        return False


while True:
    try:
        on_press()
    except:
        continue