# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /.

# Copy the requirements file into the container
COPY ./requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

EXPOSE 8000

# Set the command to run when the container starts
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
