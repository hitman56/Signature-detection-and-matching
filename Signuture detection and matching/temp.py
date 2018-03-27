# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image, ImageEnhance
def enhance_signature(img):
  bw = ImageEnhance.Color(img).enhance(2.0)
  bright = ImageEnhance.Brightness(bw).enhance(1.0)
  contrast = ImageEnhance.Contrast(bright).enhance(2.0)
  
  sign = contrast.convert("RGBA")
  datas = sign.getdata()

  newData = []
  for item in datas:
    if item[0] <  200 and item[1] > 100 and item[2] > 100:
      newData.append((255, 255, 255, 0))
    else:
      newData.append(item)

  sign.putdata(newData)
  sign.save("signature_alpha.png", "PNG")
  
def get_boxed_signature():
  img = Image.open("signature_alpha.png")
  img = img.convert("RGBA")
  pixdata = img.load()
  
  start_pixel = [img.size[0], img.size[1]]
  end_pixel = [0,0]
  
  for y in range(img.size[1]):
    for x in range(img.size[0]):
      if pixdata[x, y][0] > 150 and pixdata[x, y][1] < 100 and pixdata[x, y][2] < 100:
        if x < start_pixel[0]:
          start_pixel[0] = x
        if y < start_pixel[1]:
          start_pixel[1] = y
        if x > end_pixel[0]:
          end_pixel[0] = x
        if y > end_pixel[1]:
          end_pixel[1] = y
  
  crop_box = (start_pixel[0]-20, start_pixel[1]-20, end_pixel[0]+20, end_pixel[1]+20)
  signature = img.crop(crop_box)
  signature.show()
  
if __name__ == "__main__":
  filename = 'C:\\Users\\Hp\\Desktop\\Signuture detection and matching\\sign3.jpg'
#  filename = str(input("Where is your signature click?"))
  img = Image.open(filename)
  enhance_signature(img)
  get_boxed_signature()
