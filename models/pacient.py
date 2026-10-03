from collections import deque


class Pacient:
    def __init__(self, id_pacient, name, phone, client_type, medical_appointments: deque):
        self.id_pacient = id_pacient
        self.name = name
        self.phone = phone
        self.client_type = client_type
        self.medical_appointments = medical_appointments


    def __repr__(self):
        return (
            f"Pacient(id_pacient={self.id_pacient}, name={self.name}, "
            f"phone={self.phone}, client_type={self.client_type})"
        )