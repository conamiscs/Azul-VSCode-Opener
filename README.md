# Auto VSCode opener for Azul

A plugin that automatically switches over to VS Code when you open a script in roblox studio! Specifically made for Azul as that is what I use.

# Requirements
- Python
- Roblox Studio Plugin

## Installation

Install the required python packages:

```bash
pip install fastapi uvicorn pydantic
```

# SETUP
1. Open main.py
2. Configure the script:
   - Your sync path
   - The path to your VS Code executable
   - The path to your sourcemap.json
3. Install the Roblox Studio plugin

## Roblox Studio Plugin:
https://create.roblox.com/store/asset/96825467337688/Auto-VSCode-Opener

# Usage
1. Run the Python script:
   ```bash
   python main.py
   ```
2. Open the Roblox Studio plugin
3. Enter the correct port
4. Click **Enable**
5. Open a script, it should automatically open in VS Code
