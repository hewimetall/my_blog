#!/bin/bash

docker build . -t my_blog_f
docker run --mount type=bind,src=$PWD/dist,target=/code/dist   my_blog_f