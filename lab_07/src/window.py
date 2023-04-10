from PyQt6.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem
import matplotlib.pyplot as plt

from gui import Ui_MainWindow
# from constants import *
# from cocomo import calculateProject, calculateProjectTable, calculateBudgetTable


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resizeTables()
        
        # # Get
        # self.drivers = {}
        # self.mode = {}
        # self.kloc = 0
        # self.salary = 0

        # self.ui.projectBtn.clicked.connect(self.calculateProject)
        # self.ui.taskBtn.clicked.connect(self.task)


    def resizeTables(self):
        self.ui.funcDotsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.funcDotsTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.resultFuncDotsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.resultFuncDotsTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.resultCompositionTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.resultCompositionTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.resultDevelopTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.resultDevelopTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    # # Исследовать: RELY, DATA, CPLX
    # # Проект: промежуточный
    # # Сделать для разных: SCED (normal, high, high-high)
    # def task(self):
    #     drivers = DRIVERS_VALUES
    #     kloc = 430
    #     mode = PROJECT_MODES["semidetached"]
    #     results = []

    #     for SCEDind in range(NORMAL, HIGH_HIGH + 1):
    #         drivers["SCED"] = DRIVERS_DEFAULT_VALUES["SCED"][SCEDind]

    #         resultOneValue = {
    #             "RELY": {"time": [], "work": []},
    #             "DATA": {"time": [], "work": []},
    #             "CPLX": {"time": [], "work": []},
    #         }

    #         for ind in range(LOW, HIGH_HIGH + 1): # RELY
    #             drivers["RELY"] = DRIVERS_DEFAULT_VALUES["RELY"][ind]
    #             work, time = calculateProject(drivers, mode, kloc)

    #             resultOneValue["RELY"]["work"].append(work)
    #             resultOneValue["RELY"]["time"].append(time)
    #         drivers["RELY"] = 1

    #         for ind in range(LOW, HIGH_HIGH + 1): # DATA
    #             # ind - 1, так как в DATA всего 4 значения и тогда выйдем за пределы массива
    #             # при этом значение LOW в DATA под индексом 0, а в том же RELY -- 1, 
    #             # поэтому нужно вычесть (умнее решение придумать лень)
    #             drivers["DATA"] = DRIVERS_DEFAULT_VALUES["DATA"][ind - 1]
    #             work, time = calculateProject(drivers, mode, kloc)

    #             resultOneValue["DATA"]["work"].append(work)
    #             resultOneValue["DATA"]["time"].append(time)
    #         drivers["DATA"] = 1

    #         for ind in range(LOW, HIGH_HIGH + 1): # CPLX
    #             drivers["CPLX"] = DRIVERS_DEFAULT_VALUES["CPLX"][ind]
    #             work, time = calculateProject(drivers, mode, kloc)

    #             resultOneValue["CPLX"]["work"].append(work)
    #             resultOneValue["CPLX"]["time"].append(time)
    #         drivers["CPLX"] = 1

    #         results.append(resultOneValue)

    #     self.buildGraphForTask(results)

        
    # def buildGraphForTask(self, results: list[dict[str, dict[str, list]]]):
    #     x = ['Низкий', 'Номинальный', 'Высокий', 'Очень высокий']

    #     for SCEDind, SCEDresult in enumerate(results):
    #         plt.figure(figsize=(10, 14))
    #         plt.suptitle("Исследование влияния атрибутов персонала на "
    #                         "трудозатраты и время разработки (Сложность: {})"\
    #                         .format(LEVEL_NAME[SCEDind + 2]))
            
    #         plt.subplot(121)
    #         plt.plot(x, SCEDresult["RELY"]["work"], label='RELY')
    #         plt.plot(x, SCEDresult["DATA"]["work"], label='DATA')
    #         plt.plot(x, SCEDresult["CPLX"]["work"], label='CPLX')
    #         plt.ylabel('Трудозатраты')
    #         plt.xlabel('Уровень фактора')
    #         plt.legend()
    #         plt.grid(True)

    #         plt.subplot(122)
    #         plt.plot(x, SCEDresult["RELY"]["time"], label='RELY')
    #         plt.plot(x, SCEDresult["DATA"]["time"], label='DATA')
    #         plt.plot(x, SCEDresult["CPLX"]["time"], label='CPLX')
    #         plt.ylabel('Время разработки')
    #         plt.xlabel('Уровень фактора')
    #         plt.legend()
    #         plt.grid(True)
    #         plt.show()
            

    # def calculateProject(self):
    #     self.getValues()

    #     work, time = calculateProject(self.drivers, self.mode, self.kloc)
    #     projectDict = calculateProjectTable(time, work)
    #     budgetDict = calculateBudgetTable(work, self.salary)

    #     self.fillProjectTable(projectDict)
    #     self.fillBudgetTable(budgetDict)


    # def fillProjectTable(self, projectDict: dict):
    #     self.ui.projectTable.clearContents()

    #     for ind, elem in enumerate(projectDict.values()):
    #         self.ui.projectTable.setItem(ind, WORK_PERCENT, QTableWidgetItem(str(round(elem["work%"], 2))))
    #         self.ui.projectTable.setItem(ind,         WORK, QTableWidgetItem(str(round(elem["work"], 2))))
    #         self.ui.projectTable.setItem(ind, TIME_PERCENT, QTableWidgetItem(str(round(elem["time%"], 2))))
    #         self.ui.projectTable.setItem(ind,         TIME, QTableWidgetItem(str(round(elem["time"], 2))))
    #         self.ui.projectTable.setItem(ind,    EMPLOYEES, QTableWidgetItem(str(round(elem["employees"], 2))))


    # def fillBudgetTable(self, budgetDict: dict):
    #     self.ui.budgetTable.clearContents()

    #     for ind, elem in enumerate(budgetDict.values()):
    #         self.ui.budgetTable.setItem(ind, BUDGET_PERCENT, QTableWidgetItem(str(round(elem["budget%"], 2))))
    #         self.ui.budgetTable.setItem(ind,    WORK_BUDGET, QTableWidgetItem(str(round(elem["work"], 2))))
    #         self.ui.budgetTable.setItem(ind,          MONEY, QTableWidgetItem(str(round(elem["money"], 2))))


    # def setToolTips(self):
    #     self.ui.RELYlabel.setToolTip(DRIVERS_NAMES["RELY"])
    #     self.ui.DATAlabel.setToolTip(DRIVERS_NAMES["DATA"])
    #     self.ui.CPLXlabel.setToolTip(DRIVERS_NAMES["CPLX"])
    #     self.ui.TIMElabel.setToolTip(DRIVERS_NAMES["TIME"])
    #     self.ui.STORlabel.setToolTip(DRIVERS_NAMES["STOR"])
    #     self.ui.VIRTlabel.setToolTip(DRIVERS_NAMES["VIRT"])
    #     self.ui.TURNlabel.setToolTip(DRIVERS_NAMES["TURN"])
    #     self.ui.ACAPlabel.setToolTip(DRIVERS_NAMES["ACAP"])
    #     self.ui.AEXPlabel.setToolTip(DRIVERS_NAMES["AEXP"])
    #     self.ui.PCAPlabel.setToolTip(DRIVERS_NAMES["PCAP"])
    #     self.ui.VEXPlabel.setToolTip(DRIVERS_NAMES["VEXP"])
    #     self.ui.LEXPlabel.setToolTip(DRIVERS_NAMES["LEXP"])
    #     self.ui.MODPlabel.setToolTip(DRIVERS_NAMES["MODP"])
    #     self.ui.TOOLlabel.setToolTip(DRIVERS_NAMES["TOOL"])
    #     self.ui.SCEDlabel.setToolTip(DRIVERS_NAMES["SCED"])
    #     self.ui.klocLabel.setToolTip(DRIVERS_NAMES["KLOC"])

    # def getValues(self):
    #     self.drivers = DRIVERS_VALUES
    #     self.drivers["RELY"] = DRIVERS_DEFAULT_VALUES["RELY"][self.ui.RELYvalue.currentIndex()]
    #     self.drivers["DATA"] = DRIVERS_DEFAULT_VALUES["DATA"][self.ui.DATAvalue.currentIndex()]
    #     self.drivers["CPLX"] = DRIVERS_DEFAULT_VALUES["CPLX"][self.ui.CPLXvalue.currentIndex()]
    #     self.drivers["TIME"] = DRIVERS_DEFAULT_VALUES["TIME"][self.ui.TIMEvalue.currentIndex()]
    #     self.drivers["STOR"] = DRIVERS_DEFAULT_VALUES["STOR"][self.ui.STORvalue.currentIndex()]
    #     self.drivers["VIRT"] = DRIVERS_DEFAULT_VALUES["VIRT"][self.ui.VIRTvalue.currentIndex()]
    #     self.drivers["TURN"] = DRIVERS_DEFAULT_VALUES["TURN"][self.ui.TURNvalue.currentIndex()]
    #     self.drivers["ACAP"] = DRIVERS_DEFAULT_VALUES["ACAP"][self.ui.ACAPvalue.currentIndex()]
    #     self.drivers["AEXP"] = DRIVERS_DEFAULT_VALUES["AEXP"][self.ui.AEXPvalue.currentIndex()]
    #     self.drivers["PCAP"] = DRIVERS_DEFAULT_VALUES["PCAP"][self.ui.PCAPvalue.currentIndex()]
    #     self.drivers["VEXP"] = DRIVERS_DEFAULT_VALUES["VEXP"][self.ui.VEXPvalue.currentIndex()]
    #     self.drivers["LEXP"] = DRIVERS_DEFAULT_VALUES["LEXP"][self.ui.LEXPvalue.currentIndex()]
    #     self.drivers["MODP"] = DRIVERS_DEFAULT_VALUES["MODP"][self.ui.MODPvalue.currentIndex()]
    #     self.drivers["TOOL"] = DRIVERS_DEFAULT_VALUES["TOOL"][self.ui.TOOLvalue.currentIndex()]
    #     self.drivers["SCED"] = DRIVERS_DEFAULT_VALUES["SCED"][self.ui.SCEDvalue.currentIndex()]

    #     self.mode = PROJECT_MODES[PROJECT_MODES_NAMES[self.ui.modeValue.currentIndex()]]
    #     self.kloc = self.ui.klocValue.value()
    #     self.salary = self.ui.salaryValue.value()
