import os
import my_tesseract
from flask import Flask

def print_hi(name):
   print(f'Hi, {name}')  

app = Flask(__name__)

@app.route('/')

def hello_world():
   return_str = my_tesseract.run_tesseract(r"C:\Users\SUN\Documents\ocr test folder\눈쟁이DB.PNG")
   return return_str

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print_hi('PyCharm')

   app.run(port=8000)
