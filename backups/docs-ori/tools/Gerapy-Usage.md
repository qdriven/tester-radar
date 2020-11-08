# Gerapy使用

## Installation

```shell
pip install gerapy
```

## Run Gerapy for feeds project

```shell
gerapy init feeds
cd feeds
gerapy migrate
gerapy initadmin

gerapy runserver
gerapy runserver 0.0.0.0:8888
```

- create other users:

```shell script
gerapy createsuperuser
```


## Docker Run

```shell
docker run -d -v ~/gerapy:/app/gerapy -p 8000:8000 thsheep/gerapy:master
```