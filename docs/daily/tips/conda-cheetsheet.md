---
title: conda-cheatsheet
date: 2018-09-12 13:49:17
tags:
    - cheatsheet
---

CONDA Cheat Sheet

## Conda Basics

|Command|Usage|
|-----------|-------|
|conda info|version|
|conda update conda|update conda|
|conda install <package_name>|install package|
|spyder|run a package after installed|
|conda update <package_name>|update package|

## Using Environment
|Command|Usage|
|-----------|-------|
|conda create --name py36 python=3.6|create a new python3.6 environment|
|source activate py36|activate env|
|conda env list|list all environment|
|conda create --clone <source> --name <target>|clone project|
|conda list --explicit > py36.txt|save environment to a text file|
|conda env create --file py36.txt|creat environment from a text file|
|pip install boltons|pip install to the activate environment|
|conda search PACKAGENAME|search packages|
|conda env remove --name env_name|remove environment|