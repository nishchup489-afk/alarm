from fastapi import FastAPI , Request , Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))
app.mount("/static" , StaticFiles(directory=str(BASE_DIR/"static") ) , name="static")

file = "C:\\Users\\cap34\\n12_alarm_clock\\alarm\\src\\alarm\\static\\alarm.mp3"



@app.get("/" , response_class=HTMLResponse)
def Home(request: Request):
    return templates.TemplateResponse(
        name ="index.html" , 
        request= request
    )


@app.post("/alarm", response_class=HTMLResponse)
def alarm(request: Request, alarm_time: str = Form(...)):

    try:
        validated_time = datetime.strptime(alarm_time, "%H:%M").time()
    except:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": {"status": "error"}
        })

    now = datetime.now().time()

    result = {
        "status": "success",
        "alarm_set": validated_time.strftime("%H:%M"),
        "current_time": now.strftime("%H:%M")
    }

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result
    })