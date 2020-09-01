#!/usr/bin/env bash

current_folder=`pwd`
echo $current_folder

echo "alias todo=\"python3 ${current_folder}/odo_cli.py \"" >> ~/.zshrc
source ~/.zshrc