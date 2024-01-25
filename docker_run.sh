#!/bin/bash
docker run --rm -it --gpus all --name bbox_test matsukageryo/bbox_suggestion:latest python /home/exec.py 'sample-id' 'bounding-box-suggestion'