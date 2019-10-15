import json
import sys
import threading
from PyQt5 import QtWidgets
from src.AverageDayCalculator.AverageDayCalculator import CalculateAverageDay
from AverageDaysInTestUI import Ui_Form


class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.UpdateNumber_btn.clicked.connect(self.update_button_clicked)
        self.load_average_from_json('TestDayAverageVariables.json')

    def update_average(self):
        try:
            self.ui.AverageDaysInTest_int.setText(str('Updating...'))
            self.ui.LastReportedAverage_int.setText(str('Updating...'))
            self.ui.AverageDelta_int.setText(str('Updating...'))
            TestDayAverage = CalculateAverageDay()
            TestDayAverage.Run()
            self.load_average_from_json('TestDayAverageVariables.json')
        except Exception as e:
            self.ui.AverageDaysInTest_int.setText(str('An error occured with updating. Check the console!'))
            print(e)
    
    def load_average_from_json(self,jsonfile):
        with open(jsonfile) as f:
            jsonData = json.load(f)
            averageinTestInt = self.ui.AverageDaysInTest_int
            averageDelta = self.ui.AverageDelta_int
            lastReportedDelta = self.ui.LastReportedAverage_int
            averageinTestInt.setText(str(jsonData['Current Average']))
            averageDelta.setText(str(jsonData['Average Delta']))
            lastReportedDelta.setText(str(jsonData['Last Reported Average']))
    
    def update_button_clicked(self):
        update_average_thread = threading.Thread(target=self.update_average)
        update_average_thread.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mainwindow()
    application.show()
    sys.exit(app.exec())