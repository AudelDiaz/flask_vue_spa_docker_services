FROM python:3
COPY . /src
WORKDIR /src
RUN mkdir /src/dist
RUN pip install -r requirements.txt
VOLUME [ "/src/dist" ]
EXPOSE 5000