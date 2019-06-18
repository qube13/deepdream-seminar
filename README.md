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
