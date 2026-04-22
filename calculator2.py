# calculator with multiple number inputs (using kwargs) and multiple operations at once (using BIDMAS)
from calculator2Order import StructureOrder
from functools import reduce
from tkinter import *


class Calculator:

    def __init__(self):
        pass

    def addition(self, *numbers):
        result = sum(numbers)
        # print(f"The result of your calculation is {result}")
        return result

    def subtraction(self, *numbers):
        result = reduce(lambda x, y: x - y, numbers)
        return result
        # print(f"The result of your calculation is {result}")

    def multiplication(self, *numbers):
        result = reduce(lambda x, y: x * y, numbers)
        result2 = float(("%.2f" % result))
        return result2
        # print(f"The result of your calculation is {result}")

    def division(self, *numbers):
        result = reduce(lambda x, y: x / y if y != 0 else float("inf"), numbers)
        result2 = float(("%.2f" % result))
        return result2
        # print(f"The result of your calculation is {result2}")


class Operations:
    def __init__(self):
        self.operations = {'+': calculator.addition,
                           '-': calculator.subtraction,
                           '*': calculator.multiplication,
                           '/': calculator.division}

    def calculation(self, elements):

        temp = elements
        print(elements)

        while len(elements) > 1:  # while elements has more than 1 item (the result)

            for i in range(
                    len(temp)):  # temp is a substitute list, that copies elements in order to help with iteration

                if temp[i] == '+':
                    if '*' in elements or '/' in elements:  # if there are higher priority operations in elements pass the currect one and go do it
                        pass
                    else:  # else find the numbers to the left and right of the operator and do the calculation, replace the operator index with the result, and make the numbers = None, which gets removed later
                        num1 = temp[i - 1]
                        num2 = temp[i + 1]

                        # print(num1, num2)
                        result = calculator.addition(num1, num2)
                        # print(result)

                        elements[i] = result
                        elements[i + 1] = None
                        elements[i - 1] = None
                        # print(elements)

                        break



                elif temp[i] == '-':
                    if '*' in elements or '/' in elements:
                        pass
                    else:
                        num1 = temp[i - 1]
                        num2 = temp[i + 1]

                        # print(num1, num2)
                        result = calculator.subtraction(num1, num2)

                        # print(result)
                        elements[i] = result
                        # print(elements)
                        elements[i + 1] = None
                        elements[i - 1] = None

                        break

                elif temp[i] == '*':
                    num1 = temp[i - 1]
                    num2 = temp[i + 1]

                    # print(num1, num2)
                    result = calculator.multiplication(num1, num2)

                    # print(result)
                    elements[i] = result
                    # print(elements)
                    elements[i + 1] = None
                    elements[i - 1] = None

                    break

                elif temp[i] == '/':
                    num1 = temp[i - 1]
                    num2 = temp[i + 1]

                    # print(num1, num2)
                    result = calculator.division(num1, num2)

                    # print(result)
                    elements[i] = result
                    # print(elements)
                    elements[i + 1] = None
                    elements[i - 1] = None

                    break

            while None in elements:  # remove the empty indexes
                elements.remove(None)
            print(elements)

            temp = elements.copy()  # copy elements to temp for the next iteration

            if len(elements) == 1:  # if only the result is left, return it
                return elements


calculator = Calculator()  # for calculating methods

calculation = Operations()  # for selecting correct elements to pass into the calculator


# Window for calculator

def submit():
    problem = entry.get()  # get the input from entrybox and assign to username variable

    result(problem)

    # entry.config(state=DISABLED)   #disables entrybox after submitting input


def delete():
    entry.delete(0, END)  # deletes characters from first index argument to second index argument


def backspace():  # deletes most recent letter
    entry.delete(len(entry.get()) - 1, END)


def result(problem):
    question = StructureOrder(
        problem)  # pass the input calculation into the order class, which returns the input seubdivided into numbers and operators for ease of processing
    elements = question.enqueue()  # order the elements

    result = list(calculation.calculation(elements))  # recieve the result of the input calculation
    result = result[0]
    label.config(text=f"Result: {result}")  # update the label to display answer


window = Tk()

frame = Frame(window, bg='grey', bd=5)
frame.pack(side=TOP)

entry = Entry(frame,
              font=("Arial", 40),
              bg="grey",
              fg='light blue')
# show="*")
entry.pack(side=TOP)  # pack entrybox to the top

submit_button = Button(frame, text="CALCULATE", command=submit, bg='grey', fg='light blue', padx=15, pady=10)
submit_button.pack(side=RIGHT)  # pack button to the right

delete_button = Button(frame, text="CLEAR", command=delete, bg='grey', fg='light blue', padx=15, pady=10)
delete_button.pack(side=RIGHT)  # pack button to the right

backspace_button = Button(frame, text="BACKSPACE", command=backspace, bg='grey', fg='light blue', padx=15, pady=10)
backspace_button.pack(side=RIGHT)  # pack button to the right

label = Label(frame, text="Result: ",
              font=('Arial', 30, 'bold'),
              fg='light blue',
              bg='grey',
              bd=10,
              compound='bottom')
label.pack(side=BOTTOM)

window.mainloop()