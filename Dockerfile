FROM nvidia/cuda:8.0-cudnn6-runtime

RUN apt-get update \
    && apt-get install -y wget bzip2 libx11-6 \
    && apt-get clean

RUN cd /tmp \
    && wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh \
    && /bin/bash miniconda.sh -b -p /opt/conda \
    && rm miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda install -y -q cudatoolkit numba scipy pillow

ADD . /app

WORKDIR /app
