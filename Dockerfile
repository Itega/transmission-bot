FROM python:3.10-bullseye

RUN pip install --upgrade pip

RUN adduser worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker SourceSansPro-Bold.ttf SourceSansPro-Bold.ttf

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --user --no-cache-dir -r requirements.txt

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker transmission_bot transmission_bot
COPY --chown=worker:worker config.py config.py

ENTRYPOINT ["python", "-m", "transmission_bot.main"]
