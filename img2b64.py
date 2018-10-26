import base64

def img2b64(path_to_img):
    with open(path_to_img, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string
print(img2b64('test_img.jpg'))
