# made by conamiscs!

import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# ALL SCRIPTS MUST BE SYNCED FROM ROBLOX STUDIO BEFORE YOU CAN USE THIS
# IF U OPEN A SCRIPT THAT DOESNT EXIST IN UR FILEPATH IT WILL PROBABLY BREAK IDK

FILEPATH = r"C:\YOURFILEPAHTT\sync" # REPLACE WITH YOUR SYNC LOCATION
VSCODEPATH = r"C:\Users\YOURNAME\AppData\Local\Programs\Microsoft VS Code\Code.exe" # REPLACE YOURNAME WITH UR ACCOUNT NAME

PORT = 8880

app = FastAPI()

class OpenRequest(BaseModel):
    path: str
    scripttype: str

@app.post("/open")
async def open_script(data: OpenRequest):
    pathend = ".luau"
    if data.scripttype == "Script":
        pathend = ".server.luau"
    elif data.scripttype == "LocalScript":
        pathend = ".client.luau"
    windowspath = data.path.replace(".", "\\") + pathend
    print(windowspath)
    subprocess.Popen([
        VSCODEPATH,
        "-r",
        "--goto",
        FILEPATH + "\\" + windowspath
    ])




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="localhost",
        port=PORT,
        reload=False,
        log_level="warning"
    )