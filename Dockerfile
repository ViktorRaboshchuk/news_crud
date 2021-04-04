FROM python:3.8

# create root directory for our project in the container
RUN mkdir /news_service

# Set the working directory to /music_service
WORKDIR /news_service

# Copy the current directory contents into the container at /music_service
ADD . /news_service

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
