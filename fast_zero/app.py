from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message
from fast_zero.olamundo import ola_mundo

app = FastAPI(title='Fast Zero')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/olamundo', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def on_olamundo():
    return ola_mundo()