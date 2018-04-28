FROM python:3.6

RUN apt-get update
RUN apt-get install unzip

RUN wget https://dl.bintray.com/boostorg/release/1.63.0/source/boost_1_63_0.zip
RUN unzip boost_1_63_0.zip
RUN mv boost_1_63_0 /usr/local/bin

RUN git clone https://github.com/facebookresearch/Starspace.git && cd Starspace && make
RUN cd Starspace && make query_predict

RUN pip install pexpect

COPY star_space_prediction star_space_prediction

ENTRYPOINT /bin/bash

# cd Starpsace
# bash examples/classification_ag_news.sh
