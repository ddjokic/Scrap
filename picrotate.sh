#!/bin/bash
# in terminal type sh picrotate.sh <list of files or *.EXT>, without brackets
# required is exiftool

exiftool -Orientation=1 -n "$@"