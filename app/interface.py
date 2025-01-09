from tkinter import *


class Interface:
    def __init__(self, root):
        self.root = root
        self.first_number = IntVar()


    def create_frame(self):
        self.entry = Entry(self.root, width=24, borderwidth=5, font=('Arial', 18))
        self.entry.insert(0, 0)
        # Disable mouse clicks on the widget
        self.entry.bind("<Button-1>", lambda event: "break")
        self.entry.bind("<Button-3>", lambda event: "break")

        self.button_1 = Button(self.root, text="1", padx=20, pady=15, command=lambda: self.input_number(1))
        self.button_2 = Button(self.root, text="2", padx=20, pady=15, command=lambda: self.input_number(2))
        self.button_3 = Button(self.root, text="3", padx=20, pady=15, command=lambda: self.input_number(3))
        self.button_4 = Button(self.root, text="4", padx=20, pady=15, command=lambda: self.input_number(4))
        self.button_5 = Button(self.root, text="5", padx=20, pady=15, command=lambda: self.input_number(5))
        self.button_6 = Button(self.root, text="6", padx=20, pady=15, command=lambda: self.input_number(6))
        self.button_7 = Button(self.root, text="7", padx=20, pady=15, command=lambda: self.input_number(7))
        self.button_8 = Button(self.root, text="8", padx=20, pady=15, command=lambda: self.input_number(8))
        self.button_9 = Button(self.root, text="9", padx=20, pady=15, command=lambda: self.input_number(9))
        self.button_0 = Button(self.root, text="0", padx=20, pady=15, command=lambda: self.input_number(0))

        self.button_add = Button(self.root, text="+", padx=20, pady=15, command=lambda: self.set_operator("+"))
        self.button_equal = Button(self.root, text="=", padx=21, pady=48, command=self.button_equal)
        self.button_clear = Button(self.root, text="C", padx=20, pady=15, command=lambda: self.clear(num='0'))
        self.button_all_clear = Button(self.root, text="AC", padx=16, pady=15, command=lambda: self.clear_all(clear_all=True))
        self.button_back = Button(self.root, text="<-", padx=19, pady=15, command=self.back)

        self.button_subtract = Button(self.root, text="-", padx=22, pady=15, command=lambda: self.set_operator("-"))
        self.button_multiply = Button(self.root, text="*", padx=21, pady=15, command=lambda: self.set_operator("*"))
        self.button_divide = Button(self.root, text="/", padx=22, pady=15, command=lambda: self.set_operator("/"))
        self.button_sqrt = Button(self.root, text="√", padx=21, pady=15, command=self.button_sqrt)
        self.button_percent = Button(self.root, text="%", padx=20, pady=15, command=lambda: self.set_operator("%"))
        self.button_decimal = Button(self.root, text=".", padx=22, pady=15, command=self.set_decimal)
        self.button_change_sign = Button(self.root, text="+/-", padx=15.5, pady=15)

    def show_frame(self):
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=15, sticky="nsew")

        self.button_1.grid(row=4, column=0)
        self.button_2.grid(row=4, column=1)
        self.button_3.grid(row=4, column=2)
        self.button_subtract.grid(row=4, column=3)
        self.button_equal.grid(row=4, column=4, rowspan=2, padx=5, pady=5)

        self.button_4.grid(row=3, column=0, pady=5)
        self.button_5.grid(row=3, column=1)
        self.button_6.grid(row=3, column=2)
        self.button_multiply.grid(row=3, column=3)
        self.button_percent.grid(row=3, column=4)

        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_divide.grid(row=2, column=3)
        self.button_sqrt.grid(row=2, column=4)

        self.button_0.grid(row=5, column=0, padx=5)
        self.button_decimal.grid(row=5, column=1)
        self.button_change_sign.grid(row=5, column=2, pady=5, padx=5)
        self.button_add.grid(row=5, column=3)

        self.button_clear.grid(row=1, column=2, pady=5)
        self.button_all_clear.grid(row=1, column=3)
        self.button_back.grid(row=1, column=4)
