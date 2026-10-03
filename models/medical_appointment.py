class MedicalAppointment:
    def __init__(self, attention_type, quantity, attention_priority, date):
        self.attention_type = attention_type
        self.quantity = quantity
        self.attention_priority = attention_priority
        self.date = date

    def __repr__(self):
        return (
            f"MedicalAppointment(attention_type={self.attention_type}, quantity={self.quantity}, "
            f"attention_priority={self.attention_priority}, date={self.date})"
        )