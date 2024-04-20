#Inventory using SQL
#For the login function, there should be a list of names and list of passwords

listOfNames = ['admin','admin2']
listOfPasswords = ['pw','pw2']

class MedInvSys():   
    def __init__(self, name, password):
        self.name = name #List of all the usernames 
        self.password = password #this should get the password associated with the username in sql 
    
    def userLogin(n, pw):
        for i in range(len(listOfNames)):
            if(listOfNames[i] == n and listOfPasswords[i] == pw):
                return True
        else: return False
            
    def CustomerInfo():
        return   
    
    def CustomerAdd(Customer):
        return   

    def MedicineAdd(Medicine):
        return  

    def RecordModify():
        return

    def MedicineInfo():
        return

class Inventory():
    def __init__(self, name, MedPurpose, MedExpiry, MedPrice):
        self.name = name
        self.MedPurpose = purpose
        self.MedExpiry = expirationDate
        self.MedPrice = cost

    def updateMedicineInventory(self, name, MedPurpose, MedExpiry, MedPrice):
        self.name = name
        self.MedPurpose = purpose
        self.MedExpiry = expirationDate
        self.MedPrice = cost

class Customer():
    def __init__(self, name, CusAge, CusGender, CusWeight, CusMedication):
        self.name = name
        self.CusAge = age
        self.CusGender = gender
        self.CusWeight = weight
        self.CusMedication = medication

    def updatePatientRecord(self, name, CusAge, CusGender, CusWeight, CusMedication):
        self.name = name
        self.CusAge = age
        self.CusGender = gender
        self.CusWeight = weight
        self.CusMedication = medication
