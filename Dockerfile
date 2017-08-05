FROM python:3.6.2-stretch

ADD . /restexample

RUN pip install flask
RUN pip install -e /restexample

EXPOSE 5000
CMD ["restexample"]
