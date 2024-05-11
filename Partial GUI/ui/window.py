from PyQt5.QtWidgets import QMainWindow, QTableView, QLineEdit, QLabel
from ui.UI_MainWindow import Ui_MainWindow
from bl.inventory import Inventory
from bl.inventory import Medicine
from bl.inventory import Patient


class windowUI():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)       
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)

        self.warning = self.main_win.findChild(QLabel, 'warningLabel')
        self.name = self.main_win.findChild(QLineEdit, 'nameInput')
        self.pw = self.main_win.findChild(QLineEdit, 'pwInput')
        self.greeting = self.main_win.findChild(QLabel, 'greetingLabel')

        self.amName = self.main_win.findChild(QLineEdit, 'amnameInput')
        self.amPur = self.main_win.findChild(QLineEdit, 'ampurposeInput')
        self.amExp = self.main_win.findChild(QLineEdit, 'amexpInput')
        self.amDS = self.main_win.findChild(QLineEdit, 'amdsInput')
        self.amCost = self.main_win.findChild(QLineEdit, 'amcostInput')
        self.amWarning = self.main_win.findChild(QLabel, 'amWarningLabel')

        self.umName = self.main_win.findChild(QLineEdit, 'umnameInput')
        self.umPur = self.main_win.findChild(QLineEdit, 'umpurposeInput')
        self.umExp = self.main_win.findChild(QLineEdit, 'umexpInput')
        self.umDS = self.main_win.findChild(QLineEdit, 'umdsInput')
        self.umCost = self.main_win.findChild(QLineEdit, 'umcostInput')
        self.umWarning = self.main_win.findChild(QLabel, 'umWarningLabel')

        self.vmTable = self.main_win.findChild(QTableView, 'vmTableView')

        self.apName = self.main_win.findChild(QLineEdit, 'apnameInput')
        self.apAge = self.main_win.findChild(QLineEdit, 'apageInput')
        self.apGender = self.main_win.findChild(QLineEdit, 'apgenderInput')
        self.apWeight = self.main_win.findChild(QLineEdit, 'apweightInput')
        self.apStatus = self.main_win.findChild(QLineEdit, 'apstatusInput')
        self.apMed = self.main_win.findChild(QLineEdit, 'apmedicineInput')
        self.apRem = self.main_win.findChild(QLineEdit, 'apremarksInput')
        self.apWarning = self.main_win.findChild(QLabel, 'apWarningLabel')

        self.upName = self.main_win.findChild(QLineEdit, 'upnameInput')
        self.upAge = self.main_win.findChild(QLineEdit, 'upageInput')
        self.upGender = self.main_win.findChild(QLineEdit, 'upgenderInput')
        self.upWeight = self.main_win.findChild(QLineEdit, 'upweightInput')
        self.upStatus = self.main_win.findChild(QLineEdit, 'upstatusInput')
        self.upMed = self.main_win.findChild(QLineEdit, 'upmedicineInput')
        self.upRem = self.main_win.findChild(QLineEdit, 'upremarksInput')
        self.upWarning = self.main_win.findChild(QLabel, 'upWarningLabel')

        self.vpTable = self.main_win.findChild(QTableView, 'vpTableView')
        
        self.ui.loginButton.clicked.connect(self.loginClick)
        self.ui.logOutButton.clicked.connect(self.logOutClick)

        self.ui.amMenuButton.clicked.connect(self.amMenuClick)
        self.ui.addMedicineButton.clicked.connect(self.addMedicineClick)
        self.ui.amReturnButton.clicked.connect(self.menuClick)

        self.ui.umMenuButton.clicked.connect(self.umMenuClick)
        self.ui.updateMedicineButton.clicked.connect(self.updateMedicineClick)
        self.ui.umReturnButton.clicked.connect(self.menuClick)

        self.ui.vmMenuButton.clicked.connect(self.vmMenuClick)
        self.ui.vmReturnButton.clicked.connect(self.menuClick)

        self.ui.apMenuButton.clicked.connect(self.apMenuClick)
        self.ui.addPatientButton.clicked.connect(self.addPatientClick)
        self.ui.apReturnButton.clicked.connect(self.menuClick)

        self.ui.upMenuButton.clicked.connect(self.upMenuClick)
        self.ui.updatePatientButton.clicked.connect(self.updatePatientClick)
        self.ui.upReturnButton.clicked.connect(self.menuClick)

        self.ui.vpMenuButton.clicked.connect(self.vpMenuClick)
        self.ui.vpReturnButton.clicked.connect(self.menuClick)
      
    def loginClick(self):
        if(Inventory.userLogin(self.name.text(), self.pw.text())):            
            self.greeting.setText(f'Welcome, {self.name.text()}')
            self.menuClick()
        else: self.warning.setText('Invalid username or password')

    def logOutClick(self):
        self.warning.setText('')
        self.name.setText('')
        self.pw.setText('')
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)
    
    def menuClick(self):
        self.amWarning.setText('')
        self.umWarning.setText('')
        self.apWarning.setText('')
        self.upWarning.setText('')
        self.ui.stackedWidget.setCurrentWidget(self.ui.menuPage)

    def amMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.addMedicinePage)

    def addMedicineClick(self):
        if not self.amName.text():
            self.amWarning.setText('Name cannot be empty!')
        else:
            self.amWarning.setText('Medicine added!')
            #insert code to add medicine
            #use self.amName, self.amPur, self.amExp, self.amDS, self.amCost

    def umMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.updateMedicinePage)

    def updateMedicineClick(self):
        if not self.umName.text():
            self.umWarning.setText('Name cannot be empty!')
        else:
            #check if medicine name is present
            #PLACEHOLDER
            found = True
            if found:
                #insert code to update medicine
                #use self.umName, self.umPur, self.umExp, self.umDS, self.umCost
                self.umWarning.setText('Medicine updated!')
            else:
                self.umWarning.setText('Medicine not found!')

    def vmMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.viewMedicinePage)
        #insert code to update self.vmTable

    def apMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.addPatientPage)

    def addPatientClick(self):
        if not self.apName.text():
            self.apWarning.setText('Name cannot be empty!')
        else:
            self.apWarning.setText('Patient added!')
            #insert code to add patient
            #use self.apName, self.apAge, self.apGender, etc.

    def upMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.updatePatientPage)

    def updatePatientClick(self):
        if not self.upName.text():
            self.upWarning.setText('Name cannot be empty!')
        else:
            #check if patient name is present
            #PLACEHOLDER
            found = True
            if found:
                #insert code to update medicine
                #use self.upName, self.upAge, self.upGender, etc.
                self.upWarning.setText('Patient updated!')
            else:
                self.upWarning.setText('Patient not found!')

    def vpMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.viewPatientPage)
        #insert code to update self.vpTable