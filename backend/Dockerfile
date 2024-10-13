# Use the official Python 3.9 image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose port 5000 to allow external access
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
