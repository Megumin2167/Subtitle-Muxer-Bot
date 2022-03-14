FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git python3-pip ffmpeg -y

RUN cd /
RUN git clone https://github.com/Megumin2167/Subtitle-Muxer-Bot
RUN cd Subtitle-Muxer-Bot
WORKDIR /Subtitle-Muxer-Bot

RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

CMD python3 muxbot.py