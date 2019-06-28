import math
from tkinter import *



def generateBaseAlphabets():
    baseAlphabets = {}
    for a, i in zip(range(65, 91), range(10, 36)):
        baseAlphabets[chr(a)] = i
    return baseAlphabets


def getValue(character):
    if not str(character).isalpha():
        if int(character) < 10:
            return character

        elif int(character) >= 10:
            for k, v in baseAlphabets.items():
                if v == int(character):
                    return k

    elif str(character).isalpha():
        return baseAlphabets[character.upper()]


def toDigits(number, base):
    digits = []
    while number > 0:
        digits.insert(0, getValue(number % base))
        number = number // base

    return digits


def toNumber(digits, base):
    number = 0
    digits.reverse()
    for i in range(0, len(digits)):
        number += int(digits[i]) * int(math.pow(base, i))
    return number


def baseConverter(number, initial, final):
    digits = []
    for character in str(number):
        digits.append(getValue(character))

    digits = toDigits(toNumber(digits, initial), final)
    return ''.join(str(digit) for digit in digits)


baseAlphabets = generateBaseAlphabets()


# print(baseConverter(685, 10, 16))


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Arbitrary Base Converter")
        self.pack(fill=BOTH, expand=1)
        self.update()

        self.windowInit()

    def windowInit(self):
        # Create main input field for number
        self.numberEntry = Entry(self, justify=CENTER)
        self.numberEntry.place(relx=0, rely=.4, anchor="w", relheight=0.3, relwidth=0.6)

        # Create fields for base inputs
        self.initalBaseEntry = Entry(self, justify=CENTER)
        self.initalBaseEntry.place(relx=.6, rely=.4, anchor="w", relheight=0.3, relwidth=0.2)

        self.finalBaseEntry = Entry(self, justify=CENTER)
        self.finalBaseEntry.place(relx=.8, rely=.4, anchor="w", relheight=0.3, relwidth=0.2)

        # Create button to submit
        self.submitButton = Button(self, text="Convert Number")
        self.submitButton.place(relx=0.6, rely=0.55, relwidth=0.4, relheight=0.5, anchor="nw")


root = Tk()
root.geometry("300x100")
app = Window(root)
root.mainloop()
app.mainloop()
