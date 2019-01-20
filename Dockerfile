FROM python:alpine3.7

# Pillow dependencies
RUN apk add jpeg-dev \
            zlib-dev \
            freetype-dev \
            lcms2-dev \
            openjpeg-dev \
            tiff-dev \
            tk-dev \
            tcl-dev \
            harfbuzz-dev \
            fribidi-dev \
            # build deps
            gcc \
            musl-dev \
            python-dev python3-dev

# Install app dependencies
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r ./requirements.txt

# Set up app dir
COPY . /app
CMD python ./main.py
