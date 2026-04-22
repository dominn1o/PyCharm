"""
Split operation into elements.
iterate through the elements.
if it reaches an operation symbol, take the element to the right and left of it and perform calculation.
return the element into the list, replacing the previous 3 elements (number, operation, number)
keep iterating until 1 single element(the result) is left (reduce() function??)
somehow add priority of operations
"""


class StructureOrder:
    operations = {
        '+': 0.1,
        '-': 0.1,
        '*': 0.9,
        '/': 0.9
    }

    def __init__(self, calc):
        self.calc = calc

    def enqueue(self):

        # iterates through the input calculation and divides the numbers and operators into elements, and puts them into a queue

        global num
        queue = []
        nums = []

        calc = list(self.calc.replace(" ", ""))
        temp = list(self.calc.replace(" ", ""))

        # print(calc, '\n')

        while calc:
            char = 0

            for i in temp:
                if i in ['+', '-', '*', '/']:
                    char = i
                    break
                else:
                    # create a list of numbers before an operation symbol
                    nums.append(i)
                    calc.pop(0)

            if nums:  # Check if nums list has collected any numbers
                num = float("".join(nums))  # Convert collected digits into a single integer
                queue.append(num)  # Add the number to the queue
                if char:
                    queue.append(char)

            if calc and char:
                calc.pop(0)

            # clear the list that we add individual digits to, to prepare for next iteration
            nums.clear()

            temp = calc.copy()

        queue.append(num)  # add the last number to the list because the while loop ended while we still had leftovers in num
        queue.pop()  # remove a randomly appearing last item in queue

        # print('calc: ', calc)  # The input calculation
        # print('temp: ', temp)  # A copy of the calculation to help with iteration
        # print('nums: ', nums)  # List of collected digits in calc, that exclude operators
        # print('num: ', num)  # The nums list transformed into an integer
        # print('queue: ', queue)  # The final output, contains numbers and operators divided into elements for further calculations
        return queue

# a = structureOrder('1123 + 5345 - 4333')
# a.enqueue()