@echo off

REM so we can distinguish this script's output from dockers/our app's
SET prefix=DOCKER HELPER:

REM if arg 1 is build, build the container
REM IF "%1"=="build" (ECHO %prefix% Building... & docker build --tag wallpaper .)
ECHO %prefix% Building...
docker build --tag wallpaper .

ECHO %prefix% Running...
docker run --mount type=bind,source=%CD%/out,target=/app/out  --shm-size=2g -it wallpaper %*
