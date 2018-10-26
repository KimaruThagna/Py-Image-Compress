from PIL import Image
import math
# this can be used before saving images in your web application to minimize space usage
im = Image.open("test_img.jpg")
im.save("compressed.jpg", format="JPEG", quality=50)

# considering dimensions,
def Resize(path_to_pic):
    im = Image.open(path_to_pic)
    # research on best quality to use
    width, height = im.size
    if width > 600 or height > 300:
        width = width * .7 # 70% of the excess dimensions i.e 30% redcution
        height = height * .7
    im = im.resize((int(math.floor(width)), int(math.floor(height))), Image.ANTIALIAS)
    return im

Image._show(Resize('trial_img.png'))
