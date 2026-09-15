#my apikey: sk-e50a696144b041c194c9ad264850a783
import urllib.request
import getpass
import json
import time
import tkinter

def get_balance(key):
    request = urllib.request.Request(
        "https://api.deepseek.com/user/balance",
        headers = {"Authorization": "Bearer " + key}
    )
    try:
        response = urllib.request.urlopen(request)
        data = response.read()
        newdata = json.loads(data)
        total_balance = newdata["balance_infos"][0]["total_balance"]
        return total_balance
    except urllib.error.HTTPError as e:
        if e.code == 401:
            return -1
        else:
            return -2

window = tkinter.Tk()
window.title("DeepBalance")

entry = tkinter.Entry(window)
entry.pack()

label = tkinter.Label(window, text = " ")
label.pack()

def query_balance():
    api_key = entry.get()
    res = get_balance(api_key)
    label.config(text = res)

button = tkinter.Button(window, text = "Sure", command = query_balance)
button.pack()

'''
while res == -1 or res == -2:
    if res == -1:
        print("The API Key is wrong.")
    print("Try Again.")
    api_key = getpass.getpass("APIKey: ")
    res = get_balance(api_key)
'''

window.mainloop()