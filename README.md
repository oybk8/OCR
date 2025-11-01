# OCR
opencv+pytesseract实现OCR，并打包为可执行程序


具体可看CSDN: 


打包命令：
pyinstaller -F -w .\OCR.py --additional-hooks-dir hooks   --add-binary "Tesseract-OCR\tesseract.exe;."   --add-data   "Tesseract-OCR\tessdata;tessdata"
