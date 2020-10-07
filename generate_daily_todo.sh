#!/usr/bin/env bash

# shellcheck disable=SC2006
TODAY=`date '+%Y-%m-%d'`
touch docs/tasks/todo/"${TODAY}".md
echo "# ${TODAY} To Do List" > docs/tasks/todo/"${TODAY}".md
echo "-[] <Input Item hear>" >> docs/tasks/todo/"${TODAY}".md