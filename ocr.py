from PIL import Image
import pytesseract

image_path='C:\Users\SUN\Documents\ocr test folder\Test.png'
pytesseract.pytesseract.tesseract_cmd=R'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(Image.open(image_path), lang="kor")

print(text) 