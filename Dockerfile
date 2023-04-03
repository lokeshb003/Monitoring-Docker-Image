FROM alpine:latest

WORKDIR .

RUN apk update && apk upgrade && apk add python3-dev py3-pip gcc musl-dev linux-headers

COPY . .

RUN pip3 install Flask psutil plotly


EXPOSE 8080

CMD ["python3","app.py"]

