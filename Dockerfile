FROM python:3.8-slim-buster

# Update and install AWS CLI
RUN apt-get update -y && \
apt-get install -y --no-install-recommends \
awscli && \
apt-get clean \
# rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy applicstion code
COPY . /app
# Install dependencies
RUN pip3 install --upgrade pip3 && \
    pip3 install -r requirements.txt

# Defualt commands
CMD [ "python3", "app.py" ]