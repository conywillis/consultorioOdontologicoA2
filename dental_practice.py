from collections import deque

from models.medical_appointment_setting import MedicalAppointmentSetting
from utilities.constants import Constants
from utilities.custom_utils import customUtils

class DentalPractice:
    particular_cleaning= MedicalAppointmentSetting(Constants.CLIENT_TYPES[0], Constants.ATTENTION_TYPES[0], 80000, 60000)
    particular_calza= MedicalAppointmentSetting(Constants.CLIENT_TYPES[0], Constants.ATTENTION_TYPES[1], 80000, 80000)
    particular_extraction= MedicalAppointmentSetting(Constants.CLIENT_TYPES[0], Constants.ATTENTION_TYPES[2], 80000, 100000)
    particular_diagnosis= MedicalAppointmentSetting(Constants.CLIENT_TYPES[0], Constants.ATTENTION_TYPES[3], 80000, 50000)
    
    eps_cleaning= MedicalAppointmentSetting(Constants.CLIENT_TYPES[1], Constants.ATTENTION_TYPES[0], 5000, 0)
    eps_calza= MedicalAppointmentSetting(Constants.CLIENT_TYPES[1], Constants.ATTENTION_TYPES[1], 5000, 40000)
    eps_extraction= MedicalAppointmentSetting(Constants.CLIENT_TYPES[1], Constants.ATTENTION_TYPES[2], 5000, 40000)
    eps_diagnosis= MedicalAppointmentSetting(Constants.CLIENT_TYPES[1], Constants.ATTENTION_TYPES[3], 5000, 0)
    
    prepaid_cleaning= MedicalAppointmentSetting(Constants.CLIENT_TYPES[2], Constants.ATTENTION_TYPES[0], 30000, 0)
    prepaid_calza= MedicalAppointmentSetting(Constants.CLIENT_TYPES[2], Constants.ATTENTION_TYPES[1], 30000, 10000)
    prepaid_extraction= MedicalAppointmentSetting(Constants.CLIENT_TYPES[2], Constants.ATTENTION_TYPES[2], 30000, 10000)
    prepaid_diagnosis= MedicalAppointmentSetting(Constants.CLIENT_TYPES[2], Constants.ATTENTION_TYPES[3], 30000, 0)
    
    medical_appointments_settings = [
        particular_cleaning,
        particular_calza,
        particular_extraction,
        particular_diagnosis,
        eps_cleaning,
        eps_calza,
        eps_extraction,
        eps_diagnosis,
        prepaid_cleaning,
        prepaid_calza,
        prepaid_extraction,
        prepaid_diagnosis
    ]
    
    def get_value_by_client_type_attention_type(self, client_type, attention_type, quantity):
            total_value = 0
            for appointment in self.medical_appointments_settings:
                if appointment.client_type == client_type and appointment.attention_type == attention_type:
                    total_value += appointment.appointment_value + (appointment.attention_value * quantity)
                    break
            return total_value

    def calculate_appointment_value(self, pacient):
        total_value = 0
        for appointment in pacient.medical_appointments:
            total_value += self.get_value_by_client_type_attention_type(
                pacient.client_type, appointment.attention_type, appointment.quantity
            )
        return total_value

    def sort_pacients_by_date(self, pacient_list: deque):
        return sorted(pacient_list, key=customUtils.earliest_date)
    
    def sort_pacients_by_date_inner(self, pacient_list: deque, attention_type, priority):
        def appointment_date(pacient):
            appointment = customUtils.earliest_appointment_by_type_and_priority(pacient, attention_type, priority)
            return appointment.date if appointment else "9999-12-31 23:59"

        sorted_pacients = sorted(pacient_list, key=appointment_date)
        pacient_list.clear()
        pacient_list.extend(sorted_pacients)

    def sort_pacients_by_total_value(self, pacient_list: deque):
        return sorted(pacient_list, key=lambda pacient: self.calculate_appointment_value(pacient), reverse=True)

    def calculate_total_revenue(self, pacient_list: deque):
        return sum(self.calculate_appointment_value(pacient) for pacient in pacient_list)

    def count_pacients_by_attention_type(self, pacient_list: deque, attention_type):
        return sum(
            1 for pacient in pacient_list
            if any(appointment.attention_type == attention_type for appointment in pacient.medical_appointments)
        )
    
    def separate_pacients_by_type_and_priority(self, pacient_list: deque, pacient_separated_list: deque, attention_type, priority):
        for pacient in list(pacient_list):
            if any(appointment.attention_type == attention_type and appointment.attention_priority == priority for appointment in pacient.medical_appointments):
                pacient_separated_list.append(pacient)
                pacient_list.remove(pacient)
                
        