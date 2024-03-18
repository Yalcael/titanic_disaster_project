FROM python:3.12 AS builder

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

FROM python:3.12-slim AS production

WORKDIR /code

COPY --from=builder /usr/local /usr/local
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY ./titanic_disaster /code/titanic_disaster
COPY ./script/fill_database.py /code/
COPY ./main.py /code/main.py
COPY ./train.csv /code/
RUN python /code/fill_database.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]