#!/bin/bash

if [ -d "./pyinstaller" ]; then
    rm -rf ./pyinstaller
fi

mkdir ./pyinstaller
cd ./pyinstaller
pyinstaller --onefile --clean --name bbox_suggestion ../main.py --hidden-import=tf_keras.src.engine.base_layer_v1 --add-binary "/usr/local/lib/python3.11/dist-packages/tensorflow_io/python/ops/libtensorflow_io.so:."

cp /usr/local/lib/python3.11/dist-packages/tensorflow_io/python/ops/libtensorflow_io.so ./dist