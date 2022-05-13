FROM python:3

COPY requirements/requirements.txt .

RUN pip install -r requirements.txt

#RUN sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
RUN apt-get update
RUN apt-get -y install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

ADD RTsound.py /
CMD ["python3", "RTsound.py"]


