from math import ceil
from constants import *


def calculateProjectTable(time: float, work: float):
    return {
        0: {"time%":  36, "time": time * 0.36, "work%":   8, "work": work * 0.08, "employees": ceil((work * 0.08) / (time * 0.36))},
        1: {"time%":  36, "time": time * 0.36, "work%":  18, "work": work * 0.18, "employees": ceil((work * 0.18) / (time * 0.36))},
        2: {"time%":  18, "time": time * 0.18, "work%":  25, "work": work * 0.25, "employees": ceil((work * 0.25) / (time * 0.18))},
        3: {"time%":  18, "time": time * 0.18, "work%":  26, "work": work * 0.26, "employees": ceil((work * 0.26) / (time * 0.18))},
        4: {"time%":  28, "time": time * 0.28, "work%":  31, "work": work * 0.31, "employees": ceil((work * 0.31) / (time * 0.28))},
        5: {"time%": 100, "time": time * 1.00, "work%": 100, "work": work * 1.00, "employees": ceil((work * 1.00) / (time * 1.00))},
        6: {"time%": 136, "time": time * 1.36, "work%": 108, "work": work * 1.08, "employees": ceil((work * 1.08) / (time * 1.36))},
    }


def calculateBudgetTable(work: float, salary: float):
    return {
        0: {"budget%":   4, "work": work * 0.04, "money": (work * 0.04) * salary},
        1: {"budget%":  12, "work": work * 0.12, "money": (work * 0.12) * salary},
        2: {"budget%":  44, "work": work * 0.44, "money": (work * 0.44) * salary},
        3: {"budget%":   6, "work": work * 0.06, "money": (work * 0.06) * salary},
        4: {"budget%":  14, "work": work * 0.14, "money": (work * 0.14) * salary},
        5: {"budget%":   7, "work": work * 0.07, "money": (work * 0.07) * salary},
        6: {"budget%":   7, "work": work * 0.07, "money": (work * 0.07) * salary},
        7: {"budget%":   6, "work": work * 0.06, "money": (work * 0.06) * salary},
        8: {"budget%": 100, "work": work * 1.00, "money": (work * 1.00) * salary},
    }


def calculateProject(drivers: dict, mode: dict, kloc: int):
    eaf = calcEaf(drivers)

    work = calcWork(mode, eaf, kloc)
    time = calcTime(mode, work)

    return work, time


def calcEaf(drivers: dict):
    result = 1
    
    for driverValue in drivers.values():
        result *= driverValue

    return result


def calcWork(mode: dict, eaf: float, kloc: int):
    return mode["c1"] * eaf * (kloc ** mode["p1"])


def calcTime(mode: dict, work: float):
    return mode["c2"] * (work ** mode["p2"])
