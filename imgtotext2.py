from PIL import Image
from pytesseract import pytesseract


path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_to_image = 'text.png'

pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text
text = pytesseract.image_to_string(img)

print(text)