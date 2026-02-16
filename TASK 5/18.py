from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, patient_id, name, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.diagnosis = diagnosis

    @abstractmethod
    def treatment_cost(self):
        pass


class InPatient(Patient):
    def treatment_cost(self):
        return 5000


class OutPatient(Patient):
    def treatment_cost(self):
        return 1000


if __name__ == "__main__":
    patients = [
        InPatient(1, "John", "Surgery"),
        OutPatient(2, "Sara", "Fever")
    ]

    for patient in patients:
        print(patient.name, "Cost:", patient.treatment_cost())
