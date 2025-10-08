# Healthcare Appointment Scheduling System

class HealthcareSystem:
    def __init__(self):
        self.doctors = {
            "Dr. Smith": ["10:00", "11:00", "14:00"],
            "Dr. John": ["09:00", "13:00", "15:00"]
        }
        self.appointments = {}  # patient_name -> (doctor, time)

    def show_slots(self):
        print("\nAvailable Slots:")
        for doctor, slots in self.doctors.items():
            print(f"{doctor}: {', '.join(slots) if slots else 'No slots available'}")

    def book_appointment(self, patient, doctor, time):
        if doctor in self.doctors and time in self.doctors[doctor]:
            self.doctors[doctor].remove(time)
            self.appointments[patient] = (doctor, time)
            print(f"{patient} booked with {doctor} at {time}.")
        else:
            print(" Slot not available.")

    def modify_appointment(self, patient, new_doctor, new_time):
        if patient in self.appointments:
            old_doctor, old_time = self.appointments[patient]
            self.doctors[old_doctor].append(old_time)  # free old slot
            self.book_appointment(patient, new_doctor, new_time)
        else:
            print(" No appointment found to modify.")

    def cancel_appointment(self, patient):
        if patient in self.appointments:
            doctor, time = self.appointments.pop(patient)
            self.doctors[doctor].append(time)
            print(f" {patient}'s appointment with {doctor} at {time} canceled.")
        else:
            print(" No appointment found to cancel.")

    def reminders(self):
        print("\n🔔 Appointment Reminders:")
        for patient, (doctor, time) in self.appointments.items():
            print(f"{patient}, you have an appointment with {doctor} at {time}.")

# Example usage
system = HealthcareSystem()
system.show_slots()

system.book_appointment("Priya", "Dr. Smith", "10:00")
system.book_appointment("Rahul", "Dr. John", "15:00")
system.show_slots()

system.modify_appointment("Priya", "Dr. John", "09:00")
system.reminders()

system.cancel_appointment("Rahul")
system.show_slots()
