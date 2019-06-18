import torch
from PIL import Image, ExifTags
import numpy as np
from io import BytesIO
import base64

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