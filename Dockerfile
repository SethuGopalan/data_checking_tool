FROM python:3.9-slim

WORKDIR /app

COPY . /app


RUN pip install dash pandas dash_bootstrap_components

EXPOSE 5000

CMD [ "python","check_Data.py" ]