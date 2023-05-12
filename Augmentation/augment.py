from PIL import Image 
import cv2;
import numpy as np;
from utils import *;
import os;

OUTPUT_FOLDER_PATH = "./output";
INPUT_FOLDER_PATH = "./dataset";

if(not os.path.exists(OUTPUT_FOLDER_PATH)):
    os.mkdir(OUTPUT_FOLDER_PATH);


operations = [AUGMENT.rotate  , AUGMENT.flip , AUGMENT.flipVertical , AUGMENT.contrast , AUGMENT.brighten , AUGMENT.sharpen]


def run(filename):


    img = load_image("{}/{}".format(INPUT_FOLDER_PATH, filename))
        
    save_image(operations[0](img , 10) , "{}/{}_{}".format(OUTPUT_FOLDER_PATH , "rotate_" , filename));     #roteate 10 degrees
    save_image(operations[0](img , 50) , "{}/{}_{}".format(OUTPUT_FOLDER_PATH , "rotate50_" , filename));        #rotate 50 deg
    
    save_image(operations[1](img ) , "{}/{}_{}".format(OUTPUT_FOLDER_PATH , "flip_h_" , filename));         #flip horizonta
    save_image(operations[2](img ) , "{}/{}_{}".format(OUTPUT_FOLDER_PATH , "flip_v_" , filename));     #flip vertival
    
    save_image(operations[3](img ) , "{}/{}_{}".format(OUTPUT_FOLDER_PATH , "contrast_" , filename));     #flip vertival
    save_image(operations[3](img , 5.0 ) , "{}/{}_{}".format(OUTPUT_FOLDER_PATH , "contrast_5_" , filename));     #flip vertival
    
    save_image(operations[4](img  ,3.0) , "{}/{}_{}".format(OUTPUT_FOLDER_PATH , "brighten_" , filename));     #brighten
    save_image(operations[5](img  ,4.0) , "{}/{}_{}".format(OUTPUT_FOLDER_PATH , 'sharpen_' , filename));     #sharpen





#cv2.imwrite("./dataset/3.png" , image)
files = os.listdir(INPUT_FOLDER_PATH);
for file in files:
    run(file);
