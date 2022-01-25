#!/bin/sh
SCRIPT=$(realpath "$(dirname "$0")/main.py")
source_dir=$(realpath "$1")
dest_dir=$(realpath "$2")
mkdir -p "$dest_dir"
cd "$source_dir" || exit
for file in *; do
    $SCRIPT <"$file" >"$dest_dir/$file"
done
