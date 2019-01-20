FROM python:alpine3.7
RUN apk add \
            # pillow dependencies
            jpeg-dev \
            zlib-dev \
            freetype-dev \
            lcms2-dev \
            openjpeg-dev \
            tiff-dev \
            tk-dev \
            tcl-dev \
            harfbuzz-dev \
            fribidi-dev \
            # pillow build deps
            gcc \
            musl-dev

# Install app dependencies
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r ./requirements.txt

# Set up app dir
COPY . /app
ENTRYPOINT ["python", "./wallpaper.py"]
