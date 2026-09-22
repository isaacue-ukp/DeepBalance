import urllib.request
import json
import tkinter
import os
from datetime import datetime
from chart import show_chart, update_chart

has_requested = False

def get_balance(key):
    request = urllib.request.Request(
        "https://api.deepseek.com/user/balance",
        headers = {"Authorization": "Bearer " + key}
    )
    response = urllib.request.urlopen(request)
    data = json.loads(response.read())
    return data["balance_infos"][0]["total_balance"]

if not os.path.exists("history.json"):
    with open("history.json", "w") as f:
        f.write("[]")

with open("history.json", "r") as f:
    history = json.load(f)

window = tkinter.Tk()
window.title("DeepBalance")

entry = tkinter.Entry(window)
entry.pack()

label = tkinter.Label(window, text = " ")
label.pack()

def query_balance():
    global has_requested
    api_key = entry.get()
    try:
        res = get_balance(api_key)
        label.config(text = res)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history.append({"time": time, "balance": res})
        with open("history.json", "w") as f:
            json.dump(history, f, indent = 4)
        update_chart(history, ax, canvas)
        if not has_requested:
            button.config(text = "Renew")
            has_requested = True
    except urllib.error.HTTPError as e:
        if e.code == 401:
            label.config(text = "Invalid API KEY")
        else:
            label.config(text = f"HTTP Error: {e.code}")
    window.after(300000, query_balance)

ax, canvas = show_chart(history, window)

button = tkinter.Button(window, text = "Sure", command = query_balance)
button.pack()

window.mainloop()