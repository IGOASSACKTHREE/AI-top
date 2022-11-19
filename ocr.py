#이미지 처리하는 pillow 라이브러리 불러오기
from PIL import Image

#Tesseract 라이브러리 불러오기
import pytesseract

#이미지(경로) 선택
image_path = r"이미지 경로"

#Tesseract 파일 위치
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#text 변수에 OCR 결과 저장
text = pytesseract.image_to_string(Image.open(image_path), lang="kor")

#결과 출력
print(text)
