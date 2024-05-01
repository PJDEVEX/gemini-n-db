FROM python:3.10-slim

# Update and install AWS CLI
RUN apt update -y && \
apt install awscli -y

# Set working directory
WORKDIR /app

# Copy applicstion code
COPY . /app
# Install dependencies
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 8501

# Entrypoint
ENTRYPOINT ["streamlit", "run"]

# Command to run the application
CMD ["app.py"]