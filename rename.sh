#!/bin/bash

strip_extension() {
  filename=$(basename -- "$1")
  extension="${filename##*.}"
  filename="${filename%.*}"
  echo "$filename"
}

file_type=$(file --mime-type -b "$1")

case "$file_type" in
video/mp4)
  mv "$1" "$(strip_extension "$1").mp4"
  ;;
video/x-matroska)
  mv "$1" "$(strip_extension "$1").mkv"
  ;;
video/webm)
  mv "$1" "$(strip_extension "$1").webm"
  ;;
video/x-msvideo)
  mv "$1" "$(strip_extension "$1").avi"
  ;;
video/quicktime)
  mv "$1" "$(strip_extension "$1").mov"
  ;;
*)
  echo "MIME type not supported for file $1"
  ;;
esac
