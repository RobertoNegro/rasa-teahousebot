# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.10.1

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Copy actions folder to working directory
COPY ./actions/requirements-actions.txt /app/requirements-actions.txt

RUN apt-get update && apt-get -y install gcc

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip install -r /app/requirements-actions.txt

# Copy actions folder to working directory
COPY ./actions /app/actions

COPY ./scraper /app/scraper

# By best practices, don't run the code with root user
USER 1001