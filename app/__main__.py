#!/usr/bin/python3.11
from tkinter import *
from .interface import Interface


class Calculator(Interface):
    def __init__(self, root):
        super(Calculator, self).__init__(root)
        self.root = root

        self.first_number = 0
        self.operator = None

        self.create_frame()
        self.show_frame()

    def clear(self):
        self.entry.delete(0, END)

    def parse_number(self, number):
        if isinstance(number, str) and number.startswith("0") and not "." in number:
            return int(number)
        return number

    def input_number(self, number):
        current = self.entry.get()
        self.clear()
        new_number = str(current) + str(number)
        self.entry.insert(0, self.parse_number(new_number))

    def button_equal(self):
        second_number = self.entry.get()
        computation_string = f"{self.first_number} {self.operator} {second_number}"
        self.first_number = None
        self.operator = None
        self.clear()
        result = self.format_result(eval(computation_string))
        self.entry.insert(0, result)
        print(computation_string, "+", result)


    def button_sqrt(self):
        number = self.entry.get()
        self.clear()
        result = self.format_result(int(number) ** 0.5)
        self.entry.insert(0, result) 

    def set_operator(self, operator):
        self.operator = operator
        self.first_number = self.entry.get()
        self.clear()
        print(self.operator)


    @staticmethod
    def format_result(result):
        if isinstance(result, float):
            if result.is_integer():
                return int(result)
        return result

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.title("Simple Calculator")

    window_width = 345
    window_height = 420
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the geometry dynamically
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    app = Calculator(root)
    app.run()
