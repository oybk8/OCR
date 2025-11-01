# OCR
opencv+pytesseract实现OCR，并打包为可执行程序


具体可看CSDN: 

https://blog.csdn.net/lanfeng_x/article/details/154123754?spm=1011.2124.3001.6209

https://blog.csdn.net/lanfeng_x/article/details/154234531?spm=1011.2124.3001.6209

打包命令：
pyinstaller -F -w .\OCR.py --additional-hooks-dir hooks   --add-binary "C:\Program Files\Tesseract-OCR\\*;."
   --add-data   "C:\Program Files\Tesseract-OCR\tessdata;tessdata"
