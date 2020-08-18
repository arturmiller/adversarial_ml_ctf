FROM python:3
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN python3 -c 'from torchvision import models; models.resnet50(pretrained=True)'
COPY . /app/
CMD ["python", "app/main.py"]
