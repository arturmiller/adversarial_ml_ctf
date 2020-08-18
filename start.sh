#!/bin/bash
app="adversarial_ml_ctf"
docker build -t ${app} .
docker run -it -p 5000:5000 --name=${app} ${app}
