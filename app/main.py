from typing import Union
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
<<<<<<< HEAD
    return {"Hello": "We Love Datascientest !!"}
=======
    return {"Hello": "We Love Datascientest; and we did it. We build a CI/CD Pipeline !!"}
>>>>>>> ef1fc51bc183022dde792048e40d9d7520cc28f0
