# Hiew % Docker

```sh
# create the image
docker build -t hiew .

# use hiew in a container
docker run -it --rm --net none -v .:/work hiew

# your local (host) current folder is accessible from /work in the container

# to run hiew (bash is executed when you run a container) on a sample,
# you first need to copy it near hiew32.exe (in /hiew) 
# Note: it might be possible to make wine work with absolute paths but I prefer working on copies.
cp /work/sample.bin .
hiew ./sample.bin # the function hiew is defined in the file /root/.bashrc

# you can also use a relative path
hiew ../work/sample.bin
```