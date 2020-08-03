# Gerapy使用

## Installation

```shell
pip install gerapy
```

## Run Gerapy

```shell
gerapy init
gerapy migrate
gerapy runserver
gerapy runserver 0.0.0.0:8888
```

## Docker Run

```shell
docker run -d -v ~/gerapy:/app/gerapy -p 8000:8000 thsheep/gerapy:master
```