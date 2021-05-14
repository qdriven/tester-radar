#!/bin/sh

FOLDERS="api core crud db models schemas"
for FOLDER in ${FOLDERS}
do
  mkdir -p ../app/${FOLDER}
  touch ../app/${FOLDER}/__init__.py
done