FROM python:3.8

COPY ./requirements.txt /webapp/requirements.txt
COPY ./Makefile /webapp/Makefile
COPY api/* /webapp

WORKDIR /webapp

RUN make install

ENTRYPOINT [ "make" ]

CMD [ "run" ]
