#convert images to black and white
#you need pip install Pillow

from PIL import Image

img = Image.open("image.png")
blackAndWhite = img.convert("L")
blackAndWhite.save('bw_image.png')
blackAndWhite.show()