# PYTHON 3.9 base image
FROM python:3.9

# working directory 
WORKDIR /app

# copying requirements to install
COPY requirements.txt .

# installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copying django app into working dir
COPY . .

# removes db if exists
RUN rm -f db.sqlite3

# Expose the port that Django runs on
EXPOSE 8000

# command to run when container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]