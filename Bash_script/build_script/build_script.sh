#!/bin/bash
# This script builds a ready to release build of a repository

echo "Begin building"
FIRSTLINE=`head -n 1 source/changelog.md`
read -a FIRSTLINESPLIT <<< $FIRSTLINE
VERSION=${FIRSTLINESPLIT[1]}
echo "version $VERSION"
echo "Do you want to continue?"
read -p "Y/n " PERMISSION

if [ "$PERMISSION" == "Y" ]; then
  for file in source/*; do
    if [ "$file" == "source/secretinfo.md" ]; then
      echo "$file won't be copied"
    else
      echo "Copying $file"
      cp $file build/
    fi
    cd build/
    echo "build version $version contains:"
    ls
    cd ..
  done
  
  else
  	echo "Please come back when you are ready"
fi