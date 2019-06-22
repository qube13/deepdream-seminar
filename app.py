# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from neural_style import stylize
from utils import base64_img

PORT=5050
work_dir = os.getcwd()

# define app and config upload form
app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
upload_dir = work_dir+"/uploads/"
app.config['UPLOADED_PHOTOS_DEST'] = upload_dir 

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app) 

class UploadForm(FlaskForm):
    photo = FileField(u'Choose file',validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField(u'Style')


# define what happens 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    img_paths = os.listdir('static/images')
    captions = [os.path.splitext(path)[0] for path in img_paths]
    form = UploadForm()
    if form.validate_on_submit():
        img_name = photos.save(form.photo.data)

        model_name = request.values.get("model")
        content_image = upload_dir + img_name
        model = work_dir+"/models/"+model_name+".model"
        
        output_img = stylize(content_image, model, 0)

        os.remove(content_image)
        
        file_url = base64_img(output_img)
        return render_template('finished.html',file_url=file_url)
        
    return render_template('index.html', form=form, img_urls=img_paths,
            idxs = range(len(img_paths)),captions=captions)

if __name__ == '__main__':
    app.run(port=PORT)