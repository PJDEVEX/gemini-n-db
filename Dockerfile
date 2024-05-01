FROM python:3.8-slim-buster

# Update and install AWS CLI
RUN apt update -y && \
apt install awscli -y

# Set working directory
WORKDIR /app

# Copy applicstion code
COPY . /app
# Install dependencies
RUN pip3 install -r requirements.txt

# Defualt commands
CMD [ "python3", "app.py" ]