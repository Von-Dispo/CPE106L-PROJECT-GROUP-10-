#Inventory using SQL
#For the login function, there should be a list of names and list of passwords

listOfNames = ['admin','admin2']
listOfPasswords = ['pw','pw2']



class Inventory():   

    def __init__(self, name, password):

        self.name = name #List of all the usernames 

        self.password = password #this should get the password associated with the username in sql 



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

class Medicine ():
    def __init__(self, name, purpose, expirationDate, dataStored, cost):
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
