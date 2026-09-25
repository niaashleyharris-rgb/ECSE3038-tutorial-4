from os import name

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Device(BaseModel):
    name: str
    room: str
    temp: float
    online: bool


readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]


@app.get("/devices")
def get_devices():
    return readings


@app.get("/devices/{name}")
def get_device(name: str):
    for device in readings:
        if device["name"] == name:
            return device
    raise HTTPException(status_code=404, detail="No device called " + name)


#@app.post("/devices", status_code=201)
#def create_device(device: Device):
#    new_device = device.model_dump()
#    readings.append(new_device)
#    return new_device

@app.put("/devices/{name}")
def update_device(name: str, updated_device: Device):
    for i, d in enumerate(readings):
        if d["name"] == name:
            readings[i] = updated_device.model_dump()
            return readings[i]
    raise HTTPException(status_code=404, detail="No device called " + name)
    readings.append(updated_device.model_dump())
    return updated_device


@app.delete("/devices/{name}")
def delete_device(name: str):
    for device in readings:
        if device["name"] == name:
            readings.remove(device)
            return {"deleted": name}
    raise HTTPException(status_code=404, detail="No device called " + name)

    #write a new post handler that loops over readings and if a device is found that already has the same name then raise a 409 status code http exception, otherwise append and return a 201   
@app.post("/devices", status_code=201)
def create_device(device: Device):
    new_device = device.model_dump()
    for existing_device in readings:
        if existing_device["name"] == new_device["name"]:
            raise HTTPException(status_code=409, detail="A device called " + new_device["name"] + " already exists")
    readings.append(new_device)
    return new_device       

