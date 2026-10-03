class MedicalAppointmentSetting:
    def __init__(self, client_type, attention_type, appointment_value, attention_value):
        self.client_type = client_type
        self.attention_type = attention_type
        self.appointment_value = appointment_value
        self.attention_value = attention_value
        

    def __repr__(self):
        return (
            f"MedicalAppointment(client_type={self.client_type}, "
            f"attention_type={self.attention_type}, "
            f"appointment_value={self.appointment_value}, "
            f"attention_value={self.attention_value})"
        )