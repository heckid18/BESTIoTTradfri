from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from tradfri_controler import changeLightBrighteness, findTradfriLights
COUNT=0
## sudo uvicorn main:app --host 0.0.0.0 --port 80
## Zl5EvN4H4u75p77a

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})



@app.get("/switch/off")
async def trun_off():
    changeLightBrighteness(0)
    return "Success"


@app.get("/switch/on")
async def trun_on():
    changeLightBrighteness(200)
    return "Success"
