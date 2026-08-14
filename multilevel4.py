class hospital:
    doctor_count = 0

    def __init__(self, hospital_name):
        self.hospital_name = hospital_name

class department(hospital):
    department_name = "department"

    def __init__(self, hospital_name, department_name):
        super().__init__(hospital_name)
        self.department_name = department_name

class doctor(department):
    @classmethod
    def doctor_no(cls):
        print("Total doctors:", cls.doctor_count)

    @staticmethod
    def license_check(license_no):
        return (
            license_no.startswith("DOC")
            and len(license_no) == 8
            and license_no[3:].isdigit()
        )

    def __init__(self, hospital_name, department_name, name, license_no):
        super().__init__(hospital_name, department_name)
        self.name = name
        self.license_no = license_no
        hospital.doctor_count += 1

    def display(self):
        print(
            f"{self.hospital_name}, "
            f"{self.department_name}, "
            f"{self.name}, "
            f"{self.license_no}"
        )


h = hospital("City Hospital")

d = department("City Hospital", "Cardiology")

dr = doctor("City Hospital","Cardiology","Dr. Ravi","DOC12345")

dr.display()

doctor.doctor_no()

print(doctor.license_check("DOC12345"))
print(doctor.license_check("ABC12345"))