import os
from PIL import Image
import datetime
import matplotlib.pyplot as plt

f = "./sample"
date_string = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    resized_im = img.resize((round(img.size[0]*0.5), round(img.size[1]*0.5)))
    img_filename = file.split(".")[0]
    resized_im.save("./sample/"+img_filename+"-"+date_string+".jpg")