#!/bin/bash
lang=$1 # usually "ru"
target_dir=${2:-.} # usually source/
files=(android{,_x}.xml {ios,macos,tdesktop}.strings)

cd "$target_dir" || exit

for file in "${files[@]}"; do
    curl -sSL "https://translations.telegram.org/$lang/${file%.*}/export" -o "$file"
done
