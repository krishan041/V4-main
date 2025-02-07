FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Update system packages and install ffmpeg in a single step
RUN apt-get update && apt-get upgrade -y && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Copy the bot script
COPY . .

Expose 8080

# Set the command to run the bot
CMD ["python3", "bot.py"]
CMD gunicorn app:app & python3 bot.py
