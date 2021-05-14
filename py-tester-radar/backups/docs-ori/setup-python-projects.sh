
PROJECT=$1

pip install --user cookiecutter
mkdir ${PROJECT} && cd ${PROJECT}
mkdir {{cookiecutter.directory_name}}
touch {{cookiecutter.file_name}}.py