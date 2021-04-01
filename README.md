# NTEU Engine Builder


## A. Install

### 1. Clone the repository
```BASH
git clone https://github.com/Pangeamt/nteu_engine_builder.git
```

### 2. Install requirements
```BASH
pip install -r requirements.txt
```

## B. Instructions

## 1. Create assets
Create the "assets" directory
```BASH
python 01_create_assets.py
```

## 2. Translate function  
Edit "assets/translate.py" and adapt the "translate" function

## 3. Configuration
In  "assets/config.yaml" edit the "translationEngine" section:

### 3.1 Language code
Replace srcLang and tgtLang by appropriate language codes

### 3.2 "dockerCmds"
  - Remove the fake translation engine dependencies 
  - Add your own dependencies

### 3.3 "supervisordStartCmd"
  - Remove the fake translation engine start cmd 
  - Add your own startup command

## 4. Build dockerfile
```BASH
python 02_build_dockerfile.py
```

## E. Create the docker image
```BASH
sudo docker build -t nteu_engine_es_en ./assets
```

## E. Test the docker

### Run the docker container
```BASH
sudo docker run -p 10000:10000 nteu_engine_es_en 
```

### Test it with curl
```BASH
curl  -X POST -H "Content-Type: application/json" -d '{"texts": ["test"]}' http://0.0.0.0:10000/api/1.0.0/translate
```
