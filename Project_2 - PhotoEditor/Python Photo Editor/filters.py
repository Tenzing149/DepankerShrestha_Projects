import numpy as np
import cv2 
from PIL import Image

def original_filter(image, intensity):
    return image

def blured(image, intensity):
    img = np.array(image)
    blur = cv2.GaussianBlur(img, (21, 21), 0, 0)
    filtered = cv2.addWeighted(blur, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

def detailed(image, intensity):
    img = np.array(image)
    edges = cv2.Laplacian(img, cv2.CV_8U)
    filtered = cv2.addWeighted(edges, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

def black_and_white(image, intensity):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    filtered = cv2.addWeighted(bw, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

def smooth(image, intensity):
    img = np.array(image)
    filtered = cv2.bilateralFilter(img, 9, 75, 75)
    filtered = cv2.addWeighted(filtered, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

def inverted(image, intensity):
    img = np.array(image)
    inverted = cv2.bitwise_not(img)
    filtered = cv2.addWeighted(inverted, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

def apply_filter(filters, image, intensity):
    if filters == 'Original':
        return original_filter(image, intensity)
    elif filters == 'Blur':
        return blured(image, intensity)
    elif filters == 'Detail':
        return detailed(image, intensity)
    elif filters == 'Black and White':
        return black_and_white(image, intensity)
    elif filters == 'Smooth':
        return smooth(image, intensity)
    elif filters == 'Inverted':
        return inverted(image, intensity)
    else:
        return image
