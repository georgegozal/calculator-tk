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

    def clear(self, num=None):
        self.entry.delete(0, END)
        if num:
            self.entry.insert(0, num)

    def clear_all(self, clear_all=False):
        if clear_all:
            self.entry.delete(0, END)
            self.entry.insert(0, '0')
        self.first_number = 0
        self.operator = None

    def back(self):
        current = self.entry.get()
        self.clear()
        self.entry.insert(0, str(current)[:-1])

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
        if not self.operator and not self.first_number:
            return
        if self.operator == "%":
            return self.calculate_percent()

        second_number = self.entry.get()
        if not second_number:
            return
        computation_string = f"{self.first_number} {self.operator} {second_number}"
        result = self.format_result(eval(computation_string))
        self.clear()
        self.entry.insert(0, result)

    def calculate_percent(self):
        second_number = self.entry.get()
        result = (self.format_result(self.first_number) * self.format_result(second_number)) / 100
        result = self.format_result(f"{result:.1f}")
        self.clear()
        self.entry.insert(0, result)
        self.clear_all()

    def button_sqrt(self):
        number = self.entry.get()
        self.clear()
        try:
            result = self.format_result(f"{(int(number) ** 0.5):.1f}")
        except ValueError as e:
            result = self.format_result(f"{(float(number) ** 0.5):.1f}")
        self.entry.insert(0, result)

    def set_operator(self, operator):
        self.operator = operator
        self.first_number = self.entry.get()
        self.clear()

    @staticmethod
    def format_result(result):
        if float(result).is_integer():
            return int(float(result))
        return float(result)

    def set_decimal(self):
        current_number = self.entry.get()
        if not "." in current_number:
            current_number += "."
            self.clear()
            self.entry.insert(0, current_number)


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
