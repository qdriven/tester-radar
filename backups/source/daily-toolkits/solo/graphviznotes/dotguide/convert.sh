#!/usr/bin/env bash
echo "[usage]:sh convert.sh <output_file_format> <source_dot_file> <target_file>"
dot -T$1 $2 -o$3