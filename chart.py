from datetime import datetime
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as dates

def show_chart(history, window):
    times = []
    balances = []

    for record in history:
        times.append(datetime.strptime(record["time"], "%Y-%m-%d %H:%M:%S"))
        balances.append(float(record["balance"]))

    figure = plot.Figure(figsize = (6, 4))
    ax = figure.add_subplot(111)

    ax.plot(times, balances, label = "Your balances", color = "green", linestyle = "--", marker = "o")
    ax.xaxis.set_major_formatter(dates.DateFormatter("%H:%M"))
    ax.set_xlabel("time")
    ax.set_ylabel("balances")
    ax.set_title("Here are your balances")
    ax.grid(True)
    ax.legend()

    canvas = FigureCanvasTkAgg(figure, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    return ax, canvas

def update_chart(history, ax, canvas):
    times = []
    balances = []

    for record in history:
        times.append(datetime.strptime(record["time"], "%Y-%m-%d %H:%M:%S"))
        balances.append(float(record["balance"]))

    ax.clear()
    ax.plot(times, balances, label = "Your balances", color = "green", linestyle = "--", marker = "o")
    ax.xaxis.set_major_formatter(dates.DateFormatter("%H:%M"))
    ax.set_xlabel("time")
    ax.set_ylabel("balances")
    ax.set_title("Here are your balances")
    ax.grid(True)
    ax.legend()

    canvas.draw()