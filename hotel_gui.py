import tkinter as tk
import tkinter.messagebox as box
import tkinter.ttk as ttk
import tkinter.font as tkFont
from get_price import get_price


class App:
    def __init__(self, root):
        # setting title
        root.title("Hall Prices")
        # setting window size
        width = 433
        height = 424
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width,
                                    height,
                                    (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]
        self.hall_types = ["Small", "Medium", "Large"]

        # Initialize comboboxes
        self.month_box = ttk.Combobox(
            root, values=list(self.months),
            state='readonly')
        self.date_box = ttk.Combobox(
            root,
            values=list(
                self.dates("January")),
            state='readonly')
        self.hall_type_box = ttk.Combobox(
            root, values=list(self.hall_types),
            state='readonly')
        # Select 0 element
        self.month_box.current(0)
        self.date_box.current(0)
        self.hall_type_box.current(0)
        # Add event to update variables on combobox's value change event
        self.month_box.bind("<<ComboboxSelected>>", lambda f1: self.fun())
        self.date_box.bind("<<ComboboxSelected>>", lambda f2: self.fun2())
        # Initialize variables
        self.month = self.month_box.get()
        self.last_month = self.date_box.get()
        # Intialize button with command to call sample with arguments
        # self.button = tk.Button(self, text="Login", command=lambda: sample(self.area, self.country, self.entry_a.get(), self.entry_b.get()))
        # Place all controls to frame
        # self.month.pack(pady=5)
        # self.date.pack(pady=5)
        # self.button.pack()
        # self.pack()

        GButton_999 = ttk.Button(root)
        # GButton_999["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=18)
        # GButton_999["font"] = ft
        # GButton_999["fg"] = "#000000"
        # GButton_999["justify"] = "center"
        GButton_999["text"] = "Submit"
        GButton_999.place(x=180, y=300, width=121, height=30)
        GButton_999["command"] = lambda: self.show_price(
            self.hall_type_box.get(), self.month_box.get(), self.date_box.get())

        # self.hall_type=tk.Listbox(root)
        # self.hall_type_box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.hall_type_box["font"] = ft
        # self.hall_type_box["fg"] = "#333333"
        self.hall_type_box["justify"] = "center"
        self.hall_type_box.place(x=220, y=100, width=120, height=30)

        GLabel_707 = ttk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        GLabel_707["font"] = ft
        # GLabel_707["fg"] = "#333333"
        GLabel_707["justify"] = "center"
        GLabel_707["text"] = "Hall type"
        GLabel_707.place(x=100, y=100, width=100, height=30)

        GLabel_989 = ttk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        GLabel_989["font"] = ft
        # GLabel_989["fg"] = "#333333"
        GLabel_989["justify"] = "center"
        GLabel_989["text"] = "Month"
        GLabel_989.place(x=110, y=150, width=70, height=30)

        # self.month=tk.Listbox(root)
        # self.month_box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.month_box["font"] = ft
        # self.month_box["fg"] = "#333333"
        self.month_box["justify"] = "center"
        self.month_box.place(x=220, y=150, width=120, height=30)

        GLabel_292 = ttk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        GLabel_292["font"] = ft
        # GLabel_292["fg"] = "#333333"
        GLabel_292["justify"] = "center"
        GLabel_292["text"] = "Date"
        GLabel_292.place(x=110, y=200, width=70, height=30)

        # self.date=tk.Listbox(root)
        # self.date_box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.date_box["font"] = ft
        # self.date_box["fg"] = "#333333"
        self.date_box["justify"] = "center"
        self.date_box.place(x=220, y=200, width=50, height=30)

    def show_price(self, hall_type, month, date):
        price = get_price(hall_type, month, date)
        if price is None:
            # not available
            box.showinfo("info", "Sorry! couldn't get price")
        else:
            box.showinfo(
                "info",
                f"For a {hall_type} hall on {date}, {month}:\n Price: {price}")
        # print(price)

    def dates(self, month):
        if month in ["January",
                     "March",
                     "May",
                     "July",
                     "August",
                     "October",
                     "December"]:
            return list(range(1, 32))
        elif month in ["September", "April", "June", "November"]:
            return list(range(1, 31))
        else:
            # Feb
            return list(range(1, 29))

    def fun(self):
        # print("changed 1-st combobox value to: " + self.month_box.get())
        if self.last_month != self.month_box.get():
            self.date_box["values"] = self.dates(self.month_box.get())
            self.date_box.current(0)
        self.last_month = self.month_box.get()

    def fun2(self):
        self.date = self.date_box.get()




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
