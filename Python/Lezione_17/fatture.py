from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, patient: list[Paziente], doctor: Dottore):
        if doctor.isAValidDoctor():
            self.fatture = len(patient)
            self.salary = 0

        else:
            self.patient = None
            self.fatture = None
            self.salary = None
            self.doctor = None
            raise ValueError('Non è possibile creare la fattura poichè i dottore non è valido!')
        
    def getSalary(self):
        self.salary = self.doctor.getParcel() * len(self.patient)
        return self.salary
    
    def getFatture(self):
        self.fatture = len(self.patient)
        return self.fatture
    
    def addPatient(self, newPatient: Paziente):
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f'Alla lista del Dottor {self.doctor.getLastName()} è stato aggiunto il paziente {self.newPatient.get_IdCode()}')


    def removePatient(self, IdCode: str):
        self.patient.remove(IdCode)
        self.getFatture()
        self.getSalary()

        print (f'Alla lista del Dottore {self.doctor.getLastName()} è stato rimosso il paziente {IdCode}')