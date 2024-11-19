FROM python:slim
RUN pip3 install flask
RUN mkdir /home/app
WORKDIR /home/app
COPY app.py app.py
CMD ["python3" , "app.py"]

