#!/usr/bin/env bash

TODAY=`date '+%Y-%m-%d'`
touch docs/tasks/todo/${TODAY}.md
echo "# ${TODAY} To Do List" > docs/tasks/todo/${TODAY}.md
echo "-[] XXXX" >> docs/tasks/todo/${TODAY}.md