# from selenium import webdriver
# driver = webdriver.Edge('msedgedriver.exe')
# driver = webdriver.PhantomJS()
# driver.get('https://www.baidu.com')
# print(driver.current_url)

import tesserocr
from PIL import Image
image=Image.open('1.png')
print(tesserocr.image_to_text(image))

print(tesserocr.file_to_text('1.png'))