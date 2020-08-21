# Adversarial Machine Learning CTF

With the rise of Machine Learning IT Security might look different in a few years. This repository is a CTF challenge, showing a security flaw in most (all?) common artificial neural networks. They are vulnerable for adversarial images.  
This challenge not only requires from you to analyse the website, but also some data handling and number crunching is required.  
The challenge is to login into the website. The authentication is done by a Machine Learning model in the backend. It is able to identify valid users by an image from your webcam. You have solved the challenge when the website says "You are authenticated".  

![Website](https://raw.githubusercontent.com/arturmiller/adversarial_ml_ctf/master/images/website.png)

## Installation
The easiest way to install and run the webserver is by using [docker](https://docs.docker.com/get-docker/). Just pull and run the docker image.
```bash
docker pull arturmiller/adversarial_ml_ctf
docker run -it -p 5000:5000 --name=adversarial_ml_ctf arturmiller/adversarial_ml_ctf
```

Now you can access the website locally ([http://localhost:5000](http://localhost:5000)) with any browser.
I recommend to access the website from the same machine, where the container is running. For security reasons most browsers block opening the webcam if the connection is not secure (http instead of https). The only exception localhost.

## I have no webcam?
You actually don't need a webcam to solve this challenge. On Ubuntu you can create a fake webcam with v4l2loopback and pyfakewebcam.

```bash
sudo apt-get install -y v4l2loopback-dkms
pip3 install pyfakewebcam
```

Running v4l2loopback should create a fake device "/dev/video0".
```bash
sudo modprobe v4l2loopback exclusive_caps=1
```

Now you can stream images with [pyfakewebcam](https://github.com/jremmons/pyfakewebcam#usage).

## Build the image on your own
If you want to build the Docker image on your, download the source code and build it with docker.
```bash
git clone https://github.com/arturmiller/adversarial_ml_ctf.git
cd adversarial_ml_ctf
docker build -t adversarial_ml_ctf .
```

You can run the image with:
```bash
docker run -it -p 5000:5000 --name=adversarial_ml_ctf adversarial_ml_ctf
```

## Run without Docker
If you want to run the webserver without Docker you need [Python3](https://wiki.python.org/moin/BeginnersGuide/Download) on your machine.  
Then download the source code and install the dependencies:

```bash
git clone https://github.com/arturmiller/adversarial_ml_ctf.git
cd adversarial_ml_ctf
pip3 install -r /requirements.txt
```

Run the webserver with:
```bash
python3 main.py
```
