from PIL import Image
import pytesseract
img_obj=Image.open('sample2.png')
text=pytesseract.image_to_string(img_obj)
print(text)

