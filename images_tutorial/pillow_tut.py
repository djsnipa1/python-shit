from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import numpy as np
from numpy import asarray


def pillow_tut():
    image = Image.open('kolala.jpeg')

    print(image.format)
    print(image.size)
    print(image.mode)

    image.show()


def matplotlib_tut():
    image = image.imread('kolala.jpeg')

    print(image.dtype)
    print(image.shape)

    pyplot.imshow(image)
    pyplot.show()


def image2array():
    image = Image.open('kolala.jpeg')

    # convert image to numpy array
    data = asarray(image)
    print(type(data))
    # sumarize shape
    print(data.shape)

    image2 = Image.fromarray(data)
    print(type(image2))

    print(image2.mode)
    print(image2.size)

    image2.show()

    print(data)


def convert_to_grayscale():
    # #you can pass multiple arguments in single line
    im = np.array(Image.open('kolala.jpeg').convert('L'))
    print(type(im))

    gr_im = Image.fromarray(im).save('gr_kolala.png')


load_img_rz = np.array(Image.open('kolala.jpeg').resize((200, 200)))

Image.fromarray(load_img_rz).save('r_kolala.jpeg')

print("After resizing: ", load_img_rz.shape)