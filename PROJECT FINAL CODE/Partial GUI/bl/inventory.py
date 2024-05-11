#There should be a code in the DAL that creates Inventory objects using SQL

#for the purposes of login, there should be a list of names and list of passwords
listOfNames = ['admin','admin2']
listOfPasswords = ['pw','pw2']

class Inventory():   
    def __init__(self, name, password):
        self.name = name #this should be a list of all usernames (You should probably add anything that accesses the SQL database to the DAL (data access layer) folder)
        self.password = password #this should get the password associated with the username in sql (make a function in the data access layer again i think)

    def userLogin(n, pw):
        for i in range(len(listOfNames)):
            if(listOfNames[i] == n and listOfPasswords[i] == pw):
                return True
        else: return False

    def currentPatients():
        return
    
    def addPatient(patient):
        return
    
    def addMedicine(medicine):
        return
    
    def currentMembers():
        return

    def currentMedicines():
        return

class Medicine():
    def __init__(self, name, purpose, expirationDate, dateStored, cost):
        self.name = name
        self.purpose = purpose
        self.expirationDate = expirationDate
        self.dateStored = dateStored
        self.cost = cost

    def updateMedicineRecord(self, name, purpose, expirationDate, dateStored, cost):
        self.name = name
        self.purpose = purpose
        self.expirationDate = expirationDate
        self.dateStored = dateStored
        self.cost = cost

class Patient():
    def __init__(self, name, age, gender, weight, status, medicine, remarks):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.status = status
        self.medicine = medicine
        self.remarks = remarks

    def updatePatientRecord(self, name, age, gender, weight, status, medicine, remarks):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.status = status
        self.medicine = medicine
        self.remarks = remarks  
