import json
from os import path
from sys import stderr

def parse(filepath : str):
    file = open(filepath)
    if path.getsize(filepath) > 0: # Confirm the file is not empty
        data = json.load(file)
        file.close()
        return data
    stderr.write(f"FATAL ERROR: Failed to parse JSON from {filepath}")
    file.close()
    exit()


race = parse("./json/races.json")
magiclist = parse("./json/magictypes.json")















#UNUSED ATM
"""
def getCacheData(filePath: str) -> list:
    data = []
    file = open(filePath, "r") # Open the file for reading
    while True:
        line = file.readline()
        nextLine = file.readline()

        if line == '':
            break
        data.append(Magic(line.strip(), nextLine.strip()))
    file.close()
    return data


def addMagic(cachelist: list, magicname : str, magicdesc : str):
    if path.exists("magictypes.json"):
        file = open("magictypes.json", "w") # Open the file and append to it
        file.write("{")

        size = len(cachelist)
        for i in range(size):
            file.write(f"\n  \"{cachelist[i].name}\":\n  {{\n    \"Description\": \"{cachelist[i].description}\"\n  }},")
        file.write(f"\n  \"{magicname}\":\n  {{\n    \"Description\": \"{magicdesc}\"\n  }}\n}}")  
        file.close()
    else:
        file = open("magictypes.json", "x") # Create the new file
        file.write(f"{{\n  \"{magicname}\":\n  {{\n    \"Description\": \"{magicdesc}\"\n  }}\n}}")
        file.close()
    file = open(".cache", "a")
    file.write(f"\n{magicname}\n{magicdesc}")
    file.close()
"""