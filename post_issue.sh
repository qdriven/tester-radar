#!/bin/zsh

TITLE=$1
FILE_PATH=$2

LABEL="tips"
echo "cat ${FILE_PATH}"
content=`cat ${FILE_PATH}`
echo $content
gh issue create --title "${TITLE}" --label "${LABEL}" --body "${content}"