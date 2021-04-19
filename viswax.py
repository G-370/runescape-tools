import math
from runecrafting.guild import VisReport, GoldbergReportMachine
from runecrafting.constants import *

if (__name__ == '__main__'):
    report = VisReport(runeTable, runePrices, visPrice)
    machine = GoldbergReportMachine(report)
    machine.run()