# deepdream-seminar
FZI Seminar at Karlsruhe Institute of Technology about Neural Style Transfer 

## Clone repository 

```bash 
git clone https://github.com/qube13/deepdream-seminar.git
```

## Make virtualenv and install requirements 
On MacOS: 

```bash
cd deepdream-seminar
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
On Windows with Python 3.7:

Make sure, that you have the [x86-64](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe) version installed, otherwise pytorch won't work.  

```bash
cd deepdream-seminar
py -3 -m venv venv
venv\Scripts\activate
pip3 install -r requirements_windows.txt
pip3 install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp37-cp37m-win_amd64.whl
pip3 install https://download.pytorch.org/whl/cpu/torchvision-0.3.0-cp37-cp37m-win_amd64.whl
```

## Start the web-Application 

```bash
python3 app.py
```
Go to http://localhost:5050 and create your own neural style transfer images. 

## Add new neural style transfer models to the web-Application

For the training of a new model you need one style picture and a dataset of random pictures (existing models were trained with the [COCO](http://cocodataset.org/#download) train dataset from 2014, 13 GB). Visit the [pytorch fast neural style example](https://github.com/pytorch/examples/tree/master/fast_neural_style) and follow the instructions to train a new style. 

After creating the new style model, name it after the artist and seperate the names by a space (e.g. ```john doe.model```) and copy the model into the models folder. To be able to choose the model inside the web-Application you have to include the style image by copying it into the static/images folder. You have to name the style image exactly like the model (e.g. ```john doe.jpg```). 

After adding both the model and the new style image simply restart the web-Application.
