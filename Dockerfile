# Step 1: Use official Python image
FROM python:3.9-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy project files
COPY . /app

# Step 4: Upgrade pip and install dependencies with longer timeout
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt --default-timeout=100

# Step 5: Expose port
EXPOSE 5000

# Step 6: Run the app
CMD ["python", "app.py"]
