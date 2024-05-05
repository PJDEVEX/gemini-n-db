FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Since Github action is used, it is not required to \n
# clone the repo to aws instance. 

# Update and install AWS CLI
RUN apt update -y && \
apt install awscli -y


# Copy applicstion code
COPY . /app

# Install dependencies
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 8501

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Entrypoint
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]