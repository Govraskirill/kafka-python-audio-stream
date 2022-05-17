FROM python:3

COPY requirements/requirements.txt .



#RUN sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
RUN apt-get update
RUN apt-get -y install portaudio19-dev python3-pyaudio
RUN apt-get -y install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

RUN pip install -r requirements.txt

RUN apt-get install -y pulseaudio

ADD sendkeywordaudio.py /
ENTRYPOINT ["python3", "sendkeywordaudio.py", "-i"]



