FROM node
ADD . /app
WORKDIR /app
RUN npm install
RUN npm run build
EXPOSE 8080
VOLUME [ "/app/dist" ]
CMD [ "npm start" ]
