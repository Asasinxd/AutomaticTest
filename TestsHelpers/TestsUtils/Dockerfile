FROM python:3.6

WORKDIR /usr/src/tests
COPY . .
RUN pip install requests PyJWT discover nose

CMD nosetests --with-xunit --xunit-file=/output/functional_report.xml
