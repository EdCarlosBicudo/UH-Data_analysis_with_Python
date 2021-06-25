
import numpy as np
import matplotlib.pyplot as plt

def to_red(img):
    img2 = img.copy()
    img2[:, :, (1,2)] = 0
    return img2

def to_green(img):
    img2 = img.copy()
    img2[:, :, (0,2)] = 0
    return img2

def to_blue(img):
    img2 = img.copy()
    img2[:, :, (0,1)] = 0
    return img2

def to_grayscale(img):
    img2 = img.copy()
    img2 = 0.2126*img2[:, :, 0] + 0.7152*img2[:, :, 1] + 0.0722*img2[:, :, 2]
    return img2

def main():
    img = plt.imread("src/painting.png")
    gray = to_grayscale(img)
    plt.imshow(img)
    fig, ax = plt.subplots(5, 1)
    ax[0].imshow(img)
    ax[1].imshow(gray, cmap="gray")
    ax[2].imshow(to_red(img))
    ax[3].imshow(to_green(img))
    ax[4].imshow(to_blue(img))
    plt.show()


if __name__ == "__main__":
    main()
