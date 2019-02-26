FROM python:3.7.2

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN rm -f database/data.db
RUN python database/create_table.py

EXPOSE 5000

CMD ["python", "app.py"]
