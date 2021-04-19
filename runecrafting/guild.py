import math

class VisReport:
    def __init__(self, runetable, runeprices, visprice):
        self.slots = [[],[],[]]
        self.attempts = 0
        self.runeprices = runeprices
        self.runetable = runetable
        self.visprice = visprice
        self.visamount = 0

    def resetCoreState(self):
        self.slots = [[],[],[]]
        self.attempts = 0
        self.visamount = 0

    def insertSlot(self, whichSlot, whichRune):
        self.slots[whichSlot] = self.runetable[whichRune]
        self.slots[whichSlot].append(whichRune)

    def setSlots(self, rune1, rune2, rune3):
        self.insertSlot(0, rune1)
        self.insertSlot(1, rune2)
        self.insertSlot(2, rune3)

    def insertAttempt(self, slot1Rune, slot2Rune, slot3Rune, vis):
        self.setSlots(slot1Rune, slot2Rune, slot3Rune)
        self.visamount = vis
        self.attempts += 1

    def setAttempts(self, nTries):
        self.attempts = nTries

    def getRunesBill(self):
        bill = []
        if (len(self.slots) == 0): return bill
        for slot in self.slots:
            bill.append({
                'amount': slot[0] + ( slot[1] * self.attempts ),
                'rune': slot[2]
            })
        return bill
    
    def getCost(self):
        cost = 0
        runebill = self.getRunesBill()
        for consumption in runebill:
            cost += self.runeprices[consumption['rune']][0] * consumption['amount']
        return cost
    
    def getProfit(self):
        return (self.visamount * self.visprice) - self.getCost()

    def getCoreState(self):
        return {
            'slots': self.slots,
            'attempts': self.attempts,
            'visprice': self.visprice,
            'visamount': self.visamount,
        }
    
    def getRelatedState(self):
        return {
            'runetable': self.runetable,
            'runeprices': self.runeprices
        }

    def getState(self):
        core = self.getCoreState()
        related = self.getRelatedState()
        # Warning: requires python 3.9+
        return core | related

class GoldbergReportMachine:
    def __init__(self, report):
        self.report = report
        self.run()

    def info(self):
        print('''
            Goldberg VisWax Report Machine
            By: Vitae_mundi
            Version: 1.0
            Required Python: 3.9+

            To get the command list type 'help' then enter.
        ''')
    
    def help(self):
        print('''
            attempt [slot 1 rune] [slot 2 rune] [slot 3 rune] [vis amount]
            set-slot [slot] [rune]
            set-try [tries]
            help
            info
            reset
            profit
            bill
            state
        ''')

    def run(self):
        command = ''
        self.info()
        while (command != 'exit'):
            command = input('> ')
            self.parseCommand(command)

            if (command == 'exit'): exit()
            
    def parseCommand(self, input):

        terms = input.split(' ')
        command = terms.pop(0)
        args = terms

        registeredCommands = {
            'attempt': 'attempt',
            'set-slot': 'setSlot',
            'set-try': 'setTry',
            'help': 'help',
            'info': 'info',
            'reset': 'reset',
            'profit': 'profit',
            'state': 'state',
            'bill': 'bill',
            'exit': 'exit'
        }

        if (command not in registeredCommands.keys()): self.unknownCommand(command)

        getattr(self, registeredCommands[command])(*args)

    def unknownCommand(self, command):
        print('unknown command, use command "help" to see avaible commands.')

    def attempt(self, s1, s2, s3, va):
        va = int(va)
        self.report.insertAttempt(s1, s2, s3, va)
        print(f"Registered attempt with runes: {s1}, {s2}, {s3}, \n Producing: {va} vis wax")

    def setSlot(self, sx, rune):
        self.report.insertSlot(sx, rune)
        print(f"Set slot {sx} with {rune} rune")

    def setTry(self, tries):
        tries = int(tries)
        self.report.setAttempts(tries)
        print(f"Set the attempts done to {tries}")

    def reset(self):
        self.report.resetCoreState()
        print(f"Reseted state {self.report.getCoreState()} ")

    def profit(self):
        print(f"Your current profit is: {self.report.getProfit()}, \nCosting: {self.report.getCost()}")

    def exit(self):
        print("Shuttting down Goldberg Report Machine.")

    def state(self):
        print(f"Goldberg Report Machine State: \n {self.report.getCoreState()}")

    def bill(self):
        billReadable = ""
        bill = self.report.getRunesBill()
        for consumption in bill:
            billReadable += f"\n{math.floor(consumption['amount'])} {consumption['rune']}"
        print(f"With the amount of tries you did, your bill of materials will be {billReadable}")
