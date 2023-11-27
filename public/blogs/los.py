from js import document 
from pyodide import create_proxy

def runPython():
    print("you clicked me")

function_proxy = create_proxy(runPython)

document.getElementById("button").addEventListener("click", function_proxy)
