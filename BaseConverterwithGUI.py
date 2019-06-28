import math
from tkinter import *


class Converter():
    def __init__(self):

        self.baseAlphabets = self.generateBaseAlphabets()

    def generateBaseAlphabets(self):
        baseAlphabets = {}
        for a, i in zip(range(65, 91), range(10, 36)):
            baseAlphabets[chr(a)] = i
        return baseAlphabets

    def getValue(self, character):
        if not str(character).isalpha():
            if int(character) < 10:
                return int(character)

            elif int(character) >= 10:
                for k, v in self.baseAlphabets.items():
                    if v == int(character):
                        return k

        elif str(character).isalpha():
            return self.baseAlphabets[character.upper()]

    def toDigits(self, number, base):
        digits = []
        while number > 0:
            digits.insert(0, self.getValue(number % base))
            number = number // base

        return digits

    def toNumber(self, digits, base):
        number = 0
        digits.reverse()
        for i in range(0, len(digits)):
            number += (int(digits[i])) * int(math.pow(base, i))
        return number

    def baseConverter(self, number, initial, final):
        digits = []
        for character in str(number):
            digits.append(self.getValue(character))

        digits = self.toDigits(self.toNumber(digits, int(initial)), int(final))
        return ''.join(str(digit) for digit in digits)


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
        self.numberEntry.insert(0, "685")

        # Create fields for base inputs
        self.initalBaseEntry = Entry(self, justify=CENTER)
        self.initalBaseEntry.place(relx=.6, rely=.4, anchor="w", relheight=0.3, relwidth=0.2)
        self.initalBaseEntry.insert(0, "10")

        self.finalBaseEntry = Entry(self, justify=CENTER)
        self.finalBaseEntry.place(relx=.8, rely=.4, anchor="w", relheight=0.3, relwidth=0.2)
        self.finalBaseEntry.insert(0, "16")

        # Create button to submit
        self.submitButton = Button(self, overrelief=FLAT, text="Convert Number",
                                   command=(lambda: self.convertNumber(self.numberEntry.get(),
                                                                       self.initalBaseEntry.get(),
                                                                       self.finalBaseEntry.get())))
        self.submitButton.place(relx=0.6, rely=0.55, relwidth=0.4, relheight=0.5, anchor="nw")

        # Output Label
        self.outputlabel = Label(self)
        self.outputlabel.place(relx=0, rely=.75, anchor="w", relheight=0.3, relwidth=0.6)

        numberLabel = Label(self, text="Number")
        numberLabel.place(relx=0, rely=.0, anchor="nw", relheight=0.3, relwidth=0.6)

        fromLabel = Label(self, text="From")
        fromLabel.place(relx=.6, rely=.0, anchor="nw", relheight=0.3, relwidth=0.2)

        toLabel = Label(self, text="To")
        toLabel.place(relx=.8, rely=.0, anchor="nw", relheight=0.3, relwidth=0.2)

    def convertNumber(self, number, initial, final):
        if number == "" or initial == "" or final == "":
            self.outputlabel.config(text="Fill the boxes")
        else:
            baseConverter = Converter()
            answer = baseConverter.baseConverter(number, initial, final)
            if not "none" in str(answer).lower():
                self.outputlabel.config(text=str(answer))
                # print(baseConverter.baseConverter(number, initial, final))


root = Tk()
root.geometry("300x100")
app = Window(root)
root.mainloop()
app.mainloop()
