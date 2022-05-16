FROM python:3

COPY requirements/requirements.txt .

#copy all information from all project's directories
COPY . .

RUN pip install -r requirements.txt

ADD publisher.py /
CMD ["python3", "publisher.py"]

