# Kafka-python-audio-stream
Repository where you can find necessary information for work with kafka producer, publisher which allow work with audio stream, transfer audio to text and send keyword which recognise in audiostream to MongoDB.

In kafka-python-audio-stream-producer next .py files:
<ul>
  <li>RTsound.py read audiostream, transfer data into bytes and send data to kafka topic

  <li>fromaudiototext.py read audiostream and transfer audiostream to text in realtime

  <li>sendkeywordaudio.py read audiostream, transfer audiostream to text in realtime and send keyword to kafka topic
</ul>

In kafka-python-audio-stream-publisher next .py file:
<ul>
  <li>publisher.py which read data from topic with keyword and timestamp (for case sendkeywordaudio.py with define keyword words) and transfer this data to MongoDB
</ul>

<b>Work with dockerfile</b>

0. Take images from DockerHub:
<pre>
docker pull kirillgovras/kafka_audio_producer:1.0
docker pull kirillgovras/audio_publisher:1.0
</pre>

1. Also you can build images. Use next commands:
<pre>
docker build -t kirillgovras/kafka_audio_producer:1.0 .
docker build -t kirillgovras/audio_publisher:1.0 .
</pre>

2. After this you can build containers with commands:

<pre>
docker run --name audiopublisher kirillgovras/audio_publisher:1.0 
docker run -it --device /dev/snd:/dev/snd --name audio_producer kirillgovras/kafka_audio_producer:1.0 13
</pre>
where 13 - this is device number (you can specify this one with command <b>python3 -m sounddevice</b>)


