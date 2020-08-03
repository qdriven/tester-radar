#! /bin/bash

current_foler=`pwd`
echo $current_folder

echo "alias rr=\"python3 ${current_folder}/favorite_cli.py \"" >> ~/.zshrc
source ~/.zshrc
