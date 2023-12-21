FROM ubuntu
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y tzdata
RUN apt-get install python3 python3-pip wget -y
RUN pip3 install flask gunicorn flask selenium
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:mozillateam/firefox-next
RUN apt-get update && apt-get install -y firefox \
  && rm -rf /var/lib/apt/lists/*
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz
RUN tar -xvzf geckodriver*
RUN chmod +x geckodriver
RUN mv geckodriver /usr/bin/geckodriver
RUN mkdir working && cd working
COPY . .
RUN chmod +x run.sh
ENTRYPOINT /run.sh
