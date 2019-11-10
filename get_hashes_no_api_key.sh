#! /bin/bash

TIME_FILE="./Feed_Files/feed_file_"$(date "+%d-%m-%y_%H:%M:%S")".json"

curl -X POST https://api.maldatabase.com/download -H 'Authorization:{}' -H 'Accept-Encoding: gzip, deflate' --compressed -o $TIME_FILE
