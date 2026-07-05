# made by conamiscs!

import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json

# ALL SCRIPTS MUST BE SYNCED FROM ROBLOX STUDIO BEFORE YOU CAN USE THIS
# IF U OPEN A SCRIPT THAT DOESNT EXIST IN UR FILEPATH IT WILL PROBABLY BREAK IDK

FILEPATH = r"C:\yourprojectlocation" # REPLACE WITH YOUR SYNC LOCATION
VSCODEPATH = r"C:\Users\YOURNAME\AppData\Local\Programs\Microsoft VS Code\Code.exe" # REPLACE YOURNAME WITH UR ACCOUNT NAME OR REPLACE THE FILEPATH IF YOUR VSCODE EXECUTABLE IS LOCATED SOMEWHERE ELSE
SOURCEMAPPATH = r"C:\yourproject\sourcemap.json" # REPLACE WITH THE FILE PATH OF YOUR SOURCEMAP.JSON

app = FastAPI()

with open(SOURCEMAPPATH,"r",encoding="utf-8") as srcmap:
    SOURCEMAP = json.load(srcmap)
    

def findscript(node,descendants):
    if not descendants:
        return node.get("filePaths", [node.get("filePath")])[0]

    part = descendants[0]
    children = node.get("children",[])

    for child in children:
        if child["name"] == part:
            result = findscript(child,descendants[1:])
            return result
        
    return None
            


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

    descendants = data.path.split(".")
    windowspath = findscript(SOURCEMAP,descendants)
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
        port=8880,
        reload=False,
        log_level="warning"
    )