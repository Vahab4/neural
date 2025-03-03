class HospitalDepartment:
    def __init__(self, name, functions, hygiene_principles, ventilation_requirements):
        self.name = name
        self.functions = functions
        self.hygiene_principles = hygiene_principles
        self.ventilation_requirements = ventilation_requirements

    def __str__(self):
        return (f"Department: {self.name}\n"
                f"Functions: {', '.join(self.functions)}\n"
                f"Hygiene Principles: {', '.join(self.hygiene_principles)}\n"
                f"Ventilation Requirements: {self.ventilation_requirements}\n")

# Example data for hospital departments
departments = {
    "Reception": HospitalDepartment(
        name="Reception",
        functions=["Registration", "Examination", "Sanitary treatment", "Emergency care"],
        hygiene_principles=["Prevention of infectious diseases", "Isolation of infectious patients"],
        ventilation_requirements="Airflow separation for clean and dirty areas"
    ),
    "Ward Section": HospitalDepartment(
        name="Ward Section",
        functions=["Patient accommodation", "Medical procedures", "Nursing care"],
        hygiene_principles=["Single-corridor layout", "Airflow control"],
        ventilation_requirements="80 m3/hour per patient"
    ),
    "Operating Block": HospitalDepartment(
        name="Operating Block",
        functions=["Surgical operations", "Sterile zone maintenance"],
        hygiene_principles=["Separation of sterile, clean, and dirty flows", "Autonomous ventilation systems"],
        ventilation_requirements="60% exhaust from lower zone, 40% from upper zone"
    ),
    "Infectious Disease Department": HospitalDepartment(
        name="Infectious Disease Department",
        functions=["Isolation of infectious patients", "Sanitary treatment"],
        hygiene_principles=["Strict isolation protocols", "Regular disinfection"],
        ventilation_requirements="Negative pressure in isolation rooms"
    ),
    "Pediatric Department": HospitalDepartment(
        name="Pediatric Department",
        functions=["Child patient care", "Isolation from adult departments"],
        hygiene_principles=["Minimal contact between children", "Quarantine facilities"],
        ventilation_requirements="Separate ventilation for pediatric wards"
    ),
    "Maternity Department": HospitalDepartment(
        name="Maternity Department",
        functions=["Delivery", "Postpartum care"],
        hygiene_principles=["Separation of healthy and infected patients", "Cyclical operation"],
        ventilation_requirements="Mechanical supply-exhaust with positive pressure"
    )
}

# Print details of each department
for department in departments.values():
    print(department)

# Example function to check ventilation requirements
def check_ventilation(department_name, actual_airflow):
    department = departments.get(department_name)
    if department:
        required_airflow = department.ventilation_requirements
        return f"Required airflow for {department_name}: {required_airflow}\nActual airflow: {actual_airflow}"
    else:
        return "Department not found."

# Example usage
print(check_ventilation("Ward Section", "85 m3/hour"))

