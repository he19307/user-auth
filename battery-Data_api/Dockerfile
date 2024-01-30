FROM python:3.10
COPY requirements.txt /battery_api/requirements.txt
WORKDIR /battery_api
RUN pip install -r requirements.txt
COPY . /battery_api
RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]
