import matplotlib.pyplot as plt
import yfinance as yf
import tkinter as tk
from pandas.plotting import register_matplotlib_converters
from tkmacosx import Button

GREEN = "#5ACD96"

class Buttons:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def placeButton(self):
        button = Button(root, text=self.name, height=5, width=10, bg="black", fg=GREEN, activebackground=GREEN, focuscolor=GREEN, command=lambda: [get_stock_data(self.name)])
        button.grid(column=self.x, row=self.y, sticky="NSEW")


class FVRT(Buttons):

    def placeButton(self):
        button = Button(root, text=self.name, height=5, width=10, bg="black", fg=GREEN, activebackground=GREEN, focuscolor=GREEN, command=lambda: [insert_name(self.name)])
        button.grid(column=self.x, row=self.y, sticky="NSEW")


def get_stock_data(time):
    stockData = yf.Ticker(stockName.get())
    stockDataDF = stockData.history(period="1d")


    if time == "Today":
        stockDataDF = stockData.history(period="1d", interval="1m")
    elif time == "5 Days":
        stockDataDF = stockData.history(period="5d", interval="5m")
    elif time == "1 Month":
        stockDataDF = stockData.history(period="1mo", interval="30m")
    elif time == "3 Months":
        stockDataDF = stockData.history(period="3mo", interval="60m")
    elif time == "6 Months":
        stockDataDF = stockData.history(period="6mo", interval="1d")
    elif time == "YTD":
        stockDataDF = stockData.history(period="ytd", interval="1d")
    elif time == "1 Year":
        stockDataDF = stockData.history(period="1y", interval="1d")
    elif time == "2 Years":
        stockDataDF = stockData.history(period="2y", interval="1wk")
    elif time == "5 Years":
        stockDataDF = stockData.history(period="5y", interval="1mo")
    elif time == "Max":
        stockDataDF = stockData.history(period="max", interval="1mo")


    """   
    VOLUME CODE
    # y1 = stockDataDF["Volume"] 
    y1Median = statistics.median(y1)
    print(y1Median)
    for n in range(y1.size):
        if y1[n] < y1Median:
            stockDataDF["Volume"][n] = y1Median
    
    
    # ax1.plot(x, y1, label="Volume", color="g")
    """

    x = stockDataDF.index  # Stock Data = x
    y = stockDataDF["Close"]  # Only Close = y


    ax = plt.subplot()  # Create Plot

    ax.plot(x, y, color=GREEN)  # Axis, Color
    fig = plt.gcf()  # fig for later use
    fig.canvas.set_window_title("Stock Graph of " + stockName.get() + ", Interval: " + time)  # Title of Tab

    fig.set_size_inches(11, 8)  # Size of Window
    fig.patch.set_facecolor("black")  # Outside of plot color
    ax.patch.set_facecolor("black")  # Inside of plot color
    ax.tick_params(axis='x', colors='white')  # Axis color
    ax.tick_params(axis='y', colors='white')  # Axis color

    plt.plot()  # Plots graph
    plt.show()  # Shows graph


def insert_name(name):
    stockName.delete(0, 'end')
    stockName.insert(string=name, index=0)


if __name__ == '__main__':
    register_matplotlib_converters()
    root = tk.Tk()

    root.title("Stock Chart")
    root.geometry("1133x600")
    root.config(bg="black")

    for i in range(5):
        tk.Grid.rowconfigure(root, i, weight=1)
        tk.Grid.columnconfigure(root, i, weight=1)

    stockName = tk.Entry(root, justify="center", bg="black", fg=GREEN, highlightthickness=2, insertbackground=GREEN, bd=0, highlightbackground=GREEN)
    stockName.grid(row=0, columnspan=5, sticky="N")


    if True:
        f0 = FVRT("TSLA", 0, 1)
        f0.placeButton()
        f1 = FVRT("AAPL", 1, 1)
        f1.placeButton()
        f2 = FVRT("PLTR", 2, 1)
        f2.placeButton()
        f3 = FVRT("AMZN", 3, 1)
        f3.placeButton()
        f4 = FVRT("PLUG", 4, 1)
        f4.placeButton()
        f5 = FVRT("SEDG", 0, 2)
        f5.placeButton()
        f6 = FVRT("CGC", 1, 2)
        f6.placeButton()
        f7 = FVRT("XIACF", 2, 2)
        f7.placeButton()
        f8 = FVRT("FSLR", 3, 2)
        f8.placeButton()
        f9 = FVRT("DNNGY", 4, 2)
        f9.placeButton()

        b0 = Buttons("Today", 0, 3)
        b0.placeButton()
        b1 = Buttons("5 Days", 1, 3)
        b1.placeButton()
        b2 = Buttons("1 Month", 2, 3)
        b2.placeButton()
        b3 = Buttons("3 Months", 3, 3)
        b3.placeButton()
        b4 = Buttons("6 Months", 4, 3)
        b4.placeButton()
        b5 = Buttons("YTD", 0, 4)
        b5.placeButton()
        b6 = Buttons("1 Year", 1, 4)
        b6.placeButton()
        b7 = Buttons("2 Years", 2, 4)
        b7.placeButton()
        b8 = Buttons("5 Years", 3, 4)
        b8.placeButton()
        b9 = Buttons("Max", 4, 4)
        b9.placeButton()


    root.mainloop()
