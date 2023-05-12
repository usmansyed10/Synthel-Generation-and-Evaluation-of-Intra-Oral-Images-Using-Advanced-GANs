import numpy as np;
from PIL import Image ,  ImageEnhance;

def load_image(imgPath):
    
    image =  Image.open(imgPath);
    image = np.asarray(image);
    return image;

def save_image(img , imgPath):
    pilImage = Image.fromarray(img);
    pilImage.save(imgPath);


class AUGMENT:
    def __init__(self):
        pass
    
    @staticmethod
    def rotate(img , degrees=30):
        image=  Image.fromarray(img);
        image = image.rotate(degrees);
        return np.asarray(image);
    @staticmethod
    def flip(img ):
        m = Image.FLIP_LEFT_RIGHT;
        image=  Image.fromarray(img);
        vertical_img = image.transpose(method=m)

        return np.asarray(vertical_img);
    @staticmethod
    def flipVertical(img):
        m = Image.FLIP_TOP_BOTTOM;
        image=  Image.fromarray(img);
        vertical_img = image.transpose(method=m)

        return np.asarray(vertical_img);
    @staticmethod
    def contrast(img ,factor = 2.0):
        
        image=  Image.fromarray(img);
        im3 = ImageEnhance.Contrast(image);
        image = im3.enhance(factor)
        
        return np.asarray(image);
    
    @staticmethod
    def brighten(img , intensity=0.5):
        image=  Image.fromarray(img);
        

        filter = ImageEnhance.Brightness(image)
        new_image = filter.enhance(intensity);
        return  np.asarray(new_image);
    @staticmethod
    def sharpen(img , alpha=3.0 ):
        image=  Image.fromarray(img);
        im3 = ImageEnhance.Sharpness(image)
  
        # showing resultant image
        image=im3.enhance(alpha);
        return np.asarray(image);
    