FROM python:3.6.2-stretch

ADD . /restexample

RUN pip install -e /restexample
RUN pip install coverage nose nose-watch

EXPOSE 5000
CMD ["restexample"]
