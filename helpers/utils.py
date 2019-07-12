import torch
import requests
import os 
from PIL import Image, ExifTags
import numpy as np
from io import BytesIO
import base64

def init_images():

    def save_pic(url,directory,author):
        filename = directory + "/" + author + ".jpg"
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
    
    id_dict = {"otto dix": "2126E4604C97C06F4400C68B0929815B",
            "utagawa hiroshige": "999105307A8D4F80BE192E93480B13DA",
            "pablo picasso": "070DC1E34AE0BA7B20EF8BB50DC9FEF0",
            "adolf hölzel": "02A8ED8D49FCED8E8D81FE824273D0D0",
            "erich heckel": "00042A9614134A69A055F14A8B1BFA2B",
            "ernst ludwig kirchner": "3C6B85FD4D5F2176F043384C7FAE604",
            "wilhelm rudolph": "9485C7FF16974DBD9DE87C5BEAD96090",
            "theodor bohneberger": "4B4252604303B91657F115804F122B2C"
            }

    if not os.path.exists('static/images'):
        os.makedirs('static/images')

    for author,id_ in id_dict.items():
        directory = os.getcwd()+"/static/images"

        if os.path.isfile(directory+ "/{}.jpg".format(author)):
            continue
        
        img_link = "https://swbexpo.bsz-bw.de/image/sgs?id={}&img=1".format(id_)
        try:
            save_pic(img_link,directory,author)
        except Exception as e: 
            print(e)
            continue

def base64_img(output_img):
    buffered = BytesIO()
    output_img.save(buffered, format="JPEG")
    img_str = str(base64.b64encode(buffered.getvalue()))[2:-1]
    return "data:image/jpeg;base64," +  img_str

def load_image(filename):
    img = Image.open(filename)
    # rotate image based on meta information
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif=dict(img._getexif().items())

        if exif[orientation] == 3:
            img=img.rotate(180, expand=True)
        elif exif[orientation] == 6:
            img=img.rotate(270, expand=True)
        elif exif[orientation] == 8:
            img=img.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass
    
    # reduce size of photo if photo to big
    scale=100
    max_scale=1500
    if max(img.size) > max_scale:
        scale = max_scale/max(img.size) * 100
    
    # delete 4th Channel 
    if np.array(img).shape[2] > 3:
        img = np.array(img)[...,:3]
        img = Image.fromarray(img)
    
    # resize if scale was changed
    if scale < 100:
        basewidth = int(img.size[0] * scale/100)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)#.rotate(-90,expand=True)
    return img