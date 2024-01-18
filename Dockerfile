FROM python:3.9-slim

WORKDIR /usertype-image

#python scripts
COPY ./ /usertype-image/

# Run main.py
CMD ["python", "main.py"]
#Terminal Commands
#docker image build -t usertype-app:1.0 ./
# docker tag usertype-app:1.0 humxajunaid123/usertype-app:1.0