FROM alpine/git AS init
RUN git clone -b test https://github.com/Rhubaruth/RampaBotV2.git /rampabot
WORKDIR /rampabot
RUN git fetch && git pull

FROM python:3.13-slim
WORKDIR /app
COPY --from=init /rampabot .
RUN pip install -r requirements.txt
RUN mkdir -p ./logs && touch ./logs/logger.log
CMD ["python", "./main.py"]
