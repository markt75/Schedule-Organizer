from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Reader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Schedule Organizer'
        self.left = 800
        self.top = 400
        self.width = 300
        self.height = 300
        self.initUI()
    
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        appTitle = QLabel(self)
        appTitle.setText('Schedule Organizer')
        appTitle.adjustSize()
        appTitle.move(73, 20)

        info = QLabel(self)
        info.setText('Select weekly schedule \n and day to create plan')
        info.adjustSize()
        info.move(61, 70)


        button = QPushButton('Search File', self)
        button.clicked.connect(self.openDialog)
        button.move(25,150)  
        
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'full week']
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(days)
        self.comboBox.move(175, 150)

        self.check = False
        button_createPlan = QPushButton('Create Plan', self)
        
        button_createPlan.clicked.connect(self.createPlan)
 

        button_createPlan.move(100, 225)



    def openDialog(self):
        self.check = True
        options = QFileDialog.Options()
        self.file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        

        

    def createPlan(self):
        if not self.check:
            self.warning()
        else:
            Reader.main(self.file, self.comboBox.currentText())
            self.createdPlan_message()



 
    def warning(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Warning)

        dialog.setText('Select File First')
        dialog.setWindowTitle('Warning')
        dialog.setStandardButtons(QMessageBox.Ok)

        retval = dialog.exec_()

    def createdPlan_message(self):
        dialog = QMessageBox()

        dialog.setText('File has been created')
        dialog.setWindowTitle('Succes')
        dialog.setStandardButtons(QMessageBox.Ok)

        retval = dialog.exec_()

        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open('style.css').read())
    window = MainWindow()
    window.show()

    app.exec()

