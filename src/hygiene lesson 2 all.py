class HospitalHygiene:
    def __init__(self):
        # Insolation Requirements
        self.insolation = {
            "Definition": {
                "Описание": "Облучение поверхностей и пространств прямыми солнечными лучами.",
                "Description": "Exposure of surfaces and spaces to direct sunlight."
            },
            "Regimes": {
                "Minimal": {
                    "Ориентация": "С, СВ, СЗ",
                    "Применение": "Палаты интенсивной терапии, онкологические больные, реанимация.",
                    "Orientation": "North, Northeast, Northwest",
                    "Application": "Intensive care units, oncology patients, resuscitation."
                },
                "Moderate": {
                    "Ориентация": "В, Ю",
                    "Применение": "Общесоматические и инфекционные отделения.",
                    "Orientation": "East, South",
                    "Application": "General somatic and infectious departments."
                },
                "Maximum": {
                    "Ориентация": "ЮВ, ЮЗ",
                    "Применение": "Пациенты в стадии реконвалесценции, дети с рахитом, туберкулёзные и инфекционные больные.",
                    "Orientation": "Southeast, Southwest",
                    "Application": "Convalescent patients, children with rickets, tuberculosis, and infectious patients."
                }
            }
        }

        # Lighting Requirements
        self.lighting = {
            "Natural Lighting": {
                "КЕО (Коэффициент естественной освещённости)": "0.5% - 1.5%",
                "СК (Световой коэффициент)": {
                    "Палаты": "1:5 - 1:6",
                    "Смотровые и перевязочные": "1:4 - 1:5"
                },
                "KEO (Daylight Factor)": "0.5% - 1.5%",
                "SC (Light Coefficient)": {
                    "Wards": "1:5 - 1:6",
                    "Examination and Dressing Rooms": "1:4 - 1:5"
                }
            },
            "Artificial Lighting": {
                "Типы ламп": ["Лампы ЛДЦ", "Лампы ЛХЕ"],
                "Lamp Types": ["LDЦ lamps (Daylight lamps with improved color rendering)", "LXE lamps (Cold natural light lamps)"]
            },
            "Local Lighting": {
                "Рекомендации": "Ксеноновые лампы. Уровень местного освещения не должен превышать общее освещение более чем в 10 раз.",
                "Recommendations": "Xenon lamps. Local lighting level should not exceed general lighting by more than 10 times."
            }
        }

        # Microclimate Requirements
        self.microclimate = {
            "Temperature": {
                "Диапазон": "15–30 °C",
                "Разница по вертикали и горизонтали": "≤ 3 °C",
                "Range": "15–30 °C",
                "Vertical and Horizontal Difference": "≤ 3 °C"
            },
            "Humidity": {
                "Относительная влажность": "30–60%",
                "Relative Humidity": "30–60%"
            },
            "Air Velocity": {
                "Скорость движения воздуха": "0.1 – 0.2 м/сек",
                "Air Velocity": "0.1 – 0.2 m/s"
            },
            "Skin Temperature": {
                "Лоб": "33–34 °C",
                "Стопа": "30-31 °C",
                "Грудь": "34–35 °C",
                "Forehead": "33–34 °C",
                "Foot": "30-31 °C",
                "Chest": "34–35 °C"
            }
        }

        # Thermoregulation Mechanisms
        self.thermoregulation = {
            "Heat Production": {
                "Источники": ["Окисление пищевых веществ", "Мышечная работа", "Солнце, воздух, нагретые поверхности, горячая пища"],
                "Sources": ["Oxidation of nutrients", "Muscle work", "Sun, air, heated surfaces, hot food"]
            },
            "Heat Loss": {
                "Излучение": "55%",
                "Испарение": "29%",
                "Конвекция": "10–15%",
                "Кондукция": "1-5%",
                "Radiation": "55%",
                "Evaporation": "29%",
                "Convection": "10–15%",
                "Conduction": "1-5%"
            }
        }

    def display_insolation(self):
        print("Insolation Requirements:")
        for category, details in self.insolation.items():
            print(f"{category}:")
            if isinstance(details, dict):
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}:")
                    if isinstance(subdetails, dict):
                        for key, value in subdetails.items():
                            print(f"    {key}: {value}")
                    else:
                        print(f"    {subdetails}")
            else:
                print(f"  {details}")

    def display_lighting(self):
        print("\nLighting Requirements:")
        for category, details in self.lighting.items():
            print(f"{category}:")
            if isinstance(details, dict):
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}: {subdetails}")
            else:
                print(f"  {details}")

    def display_microclimate(self):
        print("\nMicroclimate Requirements:")
        for category, details in self.microclimate.items():
            print(f"{category}:")
            if isinstance(details, dict):
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}: {subdetails}")
            else:
                print(f"  {details}")

    def display_thermoregulation(self):
        print("\nThermoregulation Mechanisms:")
        for category, details in self.thermoregulation.items():
            print(f"{category}:")
            if isinstance(details, dict):
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}: {subdetails}")
            else:
                print(f"  {details}")


# Create an instance of the HospitalHygiene class
hospital_hygiene = HospitalHygiene()

# Display all information
hospital_hygiene.display_insolation()
hospital_hygiene.display_lighting()
hospital_hygiene.display_microclimate()
hospital_hygiene.display_thermoregulation()


class HospitalInternalEnvironment:
    def __init__(self):
        # Air Quality Requirements
        self.air_quality = {
            "Carbon Dioxide (CO2)": {
                "Допустимое содержание": "0.07% (0.73 л/м³)",
                "Permissible Level": "0.07% (0.73 l/m³)"
            },
            "Chemical Pollutants": {
                "Требования": "Не более ПДК (предельно допустимая концентрация).",
                "Requirements": "Not exceeding MPC (maximum permissible concentration)."
            },
            "Dust Levels": {
                "Чистый воздух": "≤ 0.1 мг/м³",
                "Умеренно загрязненный": "≤ 4 мг/м³",
                "Сильно загрязненный": "> 8 мг/м³",
                "Clean Air": "≤ 0.1 mg/m³",
                "Moderately Polluted": "≤ 4 mg/m³",
                "Heavily Polluted": "> 8 mg/m³"
            },
            "Bacterial Contamination": {
                "Общее количество микроорганизмов": "Зависит от класса чистоты помещения.",
                "Золотистый стафилококк": "Не допускается.",
                "Total Microorganisms": "Depends on the cleanliness class of the room.",
                "Staphylococcus aureus": "Not allowed."
            }
        }

        # Air Disinfection Technologies
        self.air_disinfection = {
            "Ultraviolet (UV) Radiation": {
                "Описание": "Использование открытых и закрытых облучателей для обеззараживания воздуха.",
                "Description": "Use of open and closed UV irradiators for air disinfection."
            },
            "Ozone Generators": {
                "Описание": "Применение озона для дезинфекции в отсутствии людей.",
                "Description": "Use of ozone for disinfection in the absence of people."
            },
            "Air Filtration": {
                "Описание": "Использование электрофильтров, фотокаталитических фильтров и других систем.",
                "Description": "Use of electrostatic filters, photocatalytic filters, and other systems."
            }
        }

        # Interior Finishing Requirements
        self.interior_finishing = {
            "Walls": {
                "Описание": "Гладкие поверхности, устойчивые к дезинфектантам (глазурованная плитка, пластик, панели).",
                "Description": "Smooth surfaces resistant to disinfectants (glazed tiles, plastic, panels)."
            },
            "Ceilings": {
                "Описание": "Гладкие потолки, водоэмульсионные краски или подвесные потолки из неперфорированных панелей.",
                "Description": "Smooth ceilings, water-based paints, or suspended ceilings made of non-perforated panels."
            },
            "Floors": {
                "Описание": "Гладкие покрытия (керамическая плитка, линолеум, полимерцементная мастика).",
                "Description": "Smooth flooring (ceramic tiles, linoleum, polymer-cement mastic)."
            },
            "Color Scheme": {
                "Описание": "Оптимальные цвета: светло-серый, желто-зеленый, голубой. Коэффициент отражения ≥ 40%.",
                "Description": "Optimal colors: light gray, yellow-green, blue. Reflectance coefficient ≥ 40%."
            }
        }

    def display_air_quality(self):
        print("Air Quality Requirements:")
        for category, details in self.air_quality.items():
            print(f"{category}:")
            if isinstance(details, dict):
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}: {subdetails}")
            else:
                print(f"  {details}")

    def display_air_disinfection(self):
        print("\nAir Disinfection Technologies:")
        for category, details in self.air_disinfection.items():
            print(f"{category}:")
            if isinstance(details, dict):
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}: {subdetails}")
            else:
                print(f"  {details}")

    def display_interior_finishing(self):
        print("\nInterior Finishing Requirements:")
        for category, details in self.interior_finishing.items():
            print(f"{category}:")
            if isinstance(details, dict):
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}: {subdetails}")
            else:
                print(f"  {details}")


# Create an instance of the HospitalInternalEnvironment class
hospital_environment = HospitalInternalEnvironment()

# Display all information
hospital_environment.display_air_quality()
hospital_environment.display_air_disinfection()
hospital_environment.display_interior_finishing()

class HospitalInfectionPrevention:
    def __init__(self):
        # Types of Prevention
        self.prevention_types = {
            "Specific Prevention": {
                "Immunization": {
                    "Planned": ["Active", "Passive"],
                    "Emergency": ["Passive"]
                }
            },
            "Non-Specific Prevention": {
                "Architectural and Planning Measures": [
                    "Zoning of territories",
                    "Rational placement of departments by floors",
                    "Patient and staff flow management",
                    "Isolation of ward sections and operating blocks"
                ],
                "Sanitary and Anti-Epidemic Measures": [
                    "Health education",
                    "Control of hospital sanitary regime",
                    "Monitoring bacterial contamination of the hospital environment",
                    "Identification of carriers",
                    "Daily inspections",
                    "Bacteriological examination"
                ],
                "Sanitary and Technical Measures": [
                    "Ventilation",
                    "Air supply",
                    "Air conditioning",
                    "Laminar flow systems"
                ],
                "Disinfection and Sterilization Measures": [
                    "Use of chemical methods",
                    "Use of physical methods",
                    "Mechanical cleaning",
                    "UV radiation"
                ]
            }
        }

        # Hospital-Acquired Infections (HAIs)
        self.hospital_infections = {
            "Definition": "Any clinically significant disease of microbial origin that affects a patient as a result of hospitalization or seeking medical care, regardless of the appearance of symptoms during or after hospitalization, as well as infections among healthcare workers due to exposure in the workplace (WHO).",
            "Types": {
                "Infections caused by pathogenic microorganisms": "25%",
                "Hospital-acquired purulent-septic infections (HAPSI)": "75%"
            },
            "Common Pathogens": [
                "Staphylococcus",
                "Escherichia",
                "Klebsiella",
                "Enterobacter",
                "Citrobacter",
                "Serratia",
                "Pseudomonas",
                "Acinetobacter",
                "Streptococcus"
            ],
            "Transmission Mechanisms": {
                "Gram-negative bacteria": "Primarily contact-household, possibly airborne",
                "Gram-positive bacteria": "Primarily airborne, but contact-household is possible"
            },
            "Risk Factors": [
                "Formation of hospital strains",
                "Large multi-story hospital complexes",
                "Increased risk groups",
                "Aging population",
                "Artificial transmission mechanisms",
                "Activation of natural transmission mechanisms"
            ],
            "Sources of Infection": [
                "Patients with HAPSI",
                "Carriers among staff and patients",
                "Contaminated environment"
            ],
            "Prevention Measures": {
                "Source Control": [
                    "Timely identification and isolation of infected patients",
                    "Use of specific treatment methods",
                    "Hair removal before surgery"
                ],
                "Transmission Control": [
                    "Airborne: Proper ventilation, air filtration, use of masks",
                    "Contact-household: Use of disposable linens, proper hand hygiene, catheter care"
                ],
                "Susceptible Population": [
                    "Reducing hospital stay duration",
                    "Early post-operative mobilization",
                    "Rational antibiotic therapy",
                    "Use of probiotics"
                ]
            }
        }

    def display_prevention_types(self):
        print("Types of Prevention:")
        for category, details in self.prevention_types.items():
            print(f"{category}:")
            if isinstance(details, dict):
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}:")
                    if isinstance(subdetails, dict):
                        for key, value in subdetails.items():
                            print(f"    {key}: {value}")
                    else:
                        for item in subdetails:
                            print(f"    - {item}")
            else:
                print(f"  {details}")

    def display_hospital_infections(self):
        print("\nHospital-Acquired Infections (HAIs):")
        for category, details in self.hospital_infections.items():
            print(f"{category}:")
            if isinstance(details, dict):
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}:")
                    if isinstance(subdetails, dict):
                        for key, value in subdetails.items():
                            print(f"    {key}: {value}")
                    else:
                        for item in subdetails:
                            print(f"    - {item}")
            else:
                print(f"  {details}")


# Create an instance of the HospitalInfectionPrevention class
hospital_prevention = HospitalInfectionPrevention()

# Display all information
hospital_prevention.display_prevention_types()
hospital_prevention.display_hospital_infections()

# Example of structuring the data in Python

# Dictionary for temperature norms in different rooms
temperature_norms = {
    "adult_patient_rooms": {"min": 20, "max": 26},
    "maternity_wards": {"min": 20, "max": 26},
    "hypothyroidism_patient_rooms": {"min": 24, "max": 27},
    "hyperthyroidism_patient_rooms": {"min": 15, "max": 17},
    "children_rooms": {"min": 20, "max": 24},
    "postpartum_rooms": {"min": 21, "max": 23},
    "burn_patient_rooms": {"min": 21, "max": 23},
    "aseptic_rooms": {"min": 21, "max": 23},
    "premature_infant_rooms": {"min": 23, "max": 27},
    "postoperative_rooms": {"min": 21, "max": 24},
    "intensive_care_rooms": {"min": 21, "max": 24},
    "operating_rooms": {"min": 21, "max": 24},
    "small_operating_rooms": {"min": 20, "max": 24},
    "endoscopy_rooms": {"min": 20, "max": 27},
    "bronchoscopy_rooms": {"min": 22, "max": 26},
    "mri_rooms": {"min": 20, "max": 23},
    "patient_sanitation_rooms": {"min": 25, "max": 29},
}

# Dictionary for humidity norms
humidity_norms = {
    "operating_rooms": {"min": 55, "max": 60},
    "recovery_rooms": {"min": 55, "max": 60},
    "intensive_care_rooms": {"min": 55, "max": 60},
    "other_rooms": {"min": 40, "max": 60},
}

# Dictionary for air movement speed norms
air_speed_norms = {
    "all_rooms": {"min": 0.1, "max": 0.2},  # in m/s
}

# Dictionary for air quality norms
air_quality_norms = {
    "CO2_concentration": 0.07,  # in %
    "ammonia_concentration": 0.04,  # in mg/m3
    "formaldehyde_concentration": 0.003,  # in mg/m3
    "phenol_concentration": 0.003,  # in mg/m3
}

# Dictionary for bacterial contamination norms
bacterial_contamination_norms = {
    "class_A": {"before_work": 200, "during_work": 500},  # CFU/m3
    "class_B": {"before_work": 500, "during_work": 750},  # CFU/m3
    "class_C": {"before_work": None, "during_work": None},  # CFU/m3
    "class_D": {"before_work": None, "during_work": None},  # CFU/m3
}

# Example function to check if temperature is within norms
def check_temperature(room_type, actual_temp):
    norms = temperature_norms.get(room_type)
    if norms and norms["min"] <= actual_temp <= norms["max"]:
        return "Temperature is within norms."
    else:
        return "Temperature is out of norms."

# Example usage
room_type = "adult_patient_rooms"
actual_temp = 25
print(check_temperature(room_type, actual_temp))

