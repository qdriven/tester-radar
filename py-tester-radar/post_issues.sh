#!/bin/zsh

BASE_PATH='docs/daily/tips/'
FILES=$(ls ${BASE_PATH})
for i in $FILES; do
  TITLE=${i}
  FILE_PATH=${BASE_PATH}${i}
  LABEL="tips"
  echo "cat ${FILE_PATH}"
  content=$(cat ${FILE_PATH})
  echo $content
  gh issue create --title "${TITLE}" --label "${LABEL}" --body "${content}"
done
