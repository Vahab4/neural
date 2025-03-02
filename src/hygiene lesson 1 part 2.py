class MedicalFacility:
    def __init__(self):
        self.principles = [
            "Create a comfortable environment for patients by ensuring a therapeutic and protective regime.",
            "Create an optimal working environment for staff to prevent occupational diseases."
        ]
        self.hai_causes = [
            "High patient density and close staff-patient interaction.",
            "Limited ventilation in hospital complexes.",
            "Natural transmission routes (airborne, contact-based).",
            "Artificial transmission routes (invasive procedures, medical equipment).",
            "Use of immunosuppressive drugs and high-risk patients (newborns, elderly, immunocompromised)."
        ]
        self.hai_impact = [
            "Negates the success of surgeries.",
            "Increases postoperative mortality.",
            "Raises infant mortality rates."
        ]
        self.prevention = {
            "Non-Specific": {
                "Architectural": [
                    "Isolation of sections (e.g., operating rooms, wards).",
                    "Proper patient and staff flow.",
                    "Rational placement of departments across floors."
                ],
                "Sanitation": [
                    "Ventilation, air supply, air conditioning, laminar airflow systems.",
                    "Zoning of territories."
                ],
                "Anti-Epidemic": [
                    "Daily inspections.",
                    "Monitoring of sanitation protocols.",
                    "Bacterial contamination control.",
                    "Identifying carriers among staff and patients."
                ],
                "Disinfection": [
                    "Use of physical methods (e.g., high temperature, UV radiation).",
                    "Mechanical cleaning.",
                    "Bacteriological testing."
                ]
            },
            "Specific": {
                "Immunization": ["Active, passive, and emergency vaccination."],
                "Chemical Agents": ["Use of disinfectants."],
                "Health Education": ["Promoting hygiene awareness."]
            }
        }
        self.location_requirements = {
            "General": "Medical facilities should be in residential, green, or suburban areas.",
            "Proximity": {
                "General Hospitals": "Close to the population they serve.",
                "Specialized Facilities": "In suburban or green zones, at least 100 meters from residential areas."
            },
            "Noise and Pollution": "Away from railways, airports, highways, and other noise sources.",
            "Land Area": {
                "Table 1": {
                    "50 beds": "150 m² per bed",
                    "300 beds": "200 m² per bed",
                    "500-600 beds": "100 m² per bed",
                    "800-1000 beds": "80 m² per bed"
                },
                "Outpatient": "0.1 ha per 100 visits, minimum 0.5 ha per facility."
            },
            "Protective Zones": {
                "Class 1 Enterprises": "1000 meters",
                "Class 2 Enterprises": "500 meters",
                "Class 3 Enterprises": "300 meters",
                "Class 4 Enterprises": "100 meters",
                "Class 5 Enterprises": "50 meters"
            },
            "Environmental Conditions": [
                "Elevated, well-lit, dry land with gentle slopes (preferably south-facing).",
                "Soil, air, noise, and electromagnetic radiation levels must meet hygiene standards."
            ],
            "Utilities": [
                "Cold and hot water supply.",
                "Sewage systems with water quality meeting regulatory standards."
            ]
        }

    def display_principles(self):
        print("Principles for Medical Facility Design:")
        for principle in self.principles:
            print(f"- {principle}")

    def display_hai_causes(self):
        print("\nCauses of Healthcare-Associated Infections (HAIs):")
        for cause in self.hai_causes:
            print(f"- {cause}")

    def display_hai_impact(self):
        print("\nImpact of HAIs:")
        for impact in self.hai_impact:
            print(f"- {impact}")

    def display_prevention(self):
        print("\nPrevention of HAIs:")
        for category, measures in self.prevention.items():
            print(f"{category} Prevention:")
            for subcategory, details in measures.items():
                print(f"  {subcategory}:")
                for detail in details:
                    print(f"    - {detail}")

    def display_location_requirements(self):
        print("\nHygienic Requirements for Medical Facility Locations:")
        for category, details in self.location_requirements.items():
            if isinstance(details, dict):
                print(f"{category}:")
                for subcategory, subdetails in details.items():
                    print(f"  {subcategory}: {subdetails}")
            else:
                print(f"{category}: {details}")


# Create an instance of the MedicalFacility class
hospital = MedicalFacility()

# Display all information
hospital.display_principles()
hospital.display_hai_causes()
hospital.display_hai_impact()
hospital.display_prevention()
hospital.display_location_requirements()

class MedicalFacilityLayout:
    def __init__(self):
        # Functional Zones
        self.functional_zones = {
            "Лечебные корпуса для неинфекционных больных": "Non-infectious patient wards",
            "Лечебные корпуса для инфекционных больных": "Infectious patient wards",
            "Садово-парковая зона": "Garden and park zone",
            "Патологоанатомический корпус": "Pathology and morgue building",
            "Хозяйственная зона и инженерные сооружения": "Utility and engineering zone"
        }

        # Zone Requirements
        self.zone_requirements = {
            "Хозяйственная зона": {
                "Описание": "Должна располагаться с подветренной стороны относительно лечебных корпусов.",
                "Description": "Should be located on the leeward side relative to the treatment buildings."
            },
            "Патологоанатомический корпус": {
                "Описание": "Не должен просматриваться из окон палатных отделений или жилых зданий.",
                "Description": "Should not be visible from the windows of ward departments or residential buildings."
            },
            "Инфекционный корпус": {
                "Описание": "Отделяется зелеными насаждениями, имеет отдельный въезд и площадку для дезинфекции.",
                "Description": "Separated by greenery, has a separate entrance and disinfection area."
            }
        }

        # Landscaping Requirements
        self.landscaping = {
            "Зеленые насаждения": {
                "Описание": "Площадь зеленых насаждений должна составлять не менее 50% территории.",
                "Description": "Green areas should cover at least 50% of the territory."
            },
            "Защитная зеленая полоса": {
                "Описание": "Полоса шириной не менее 15 метров по периметру участка.",
                "Description": "A protective green strip at least 15 meters wide around the perimeter."
            },
            "Расстояние до зданий": {
                "Описание": "Деревья высаживаются на расстоянии не ближе 15 метров, кустарники – 5 метров от зданий.",
                "Description": "Trees should be planted at least 15 meters away, shrubs – 5 meters from buildings."
            }
        }

        # Hospital Construction Systems
        self.construction_systems = {
            "Децентрализованная система": {
                "Описание": "Отдельные корпуса для разных отделений. Подходит для инфекционных, детских и психиатрических больниц.",
                "Преимущества": [
                    "Полная изоляция пациентов.",
                    "Использование природных факторов для лечения."
                ],
                "Недостатки": [
                    "Дублирование лечебно-диагностических кабинетов.",
                    "Увеличение площади и затрат."
                ],
                "Description": "Separate buildings for different departments. Suitable for infectious, pediatric, and psychiatric hospitals.",
                "Advantages": [
                    "Complete isolation of patients.",
                    "Use of natural factors for treatment."
                ],
                "Disadvantages": [
                    "Duplication of diagnostic and treatment rooms.",
                    "Increased area and costs."
                ]
            },
            "Централизованная система": {
                "Описание": "Все отделения (кроме инфекционных и патологоанатомических) в одном здании.",
                "Преимущества": [
                    "Эффективное использование коечного фонда и персонала.",
                    "Сокращение затрат."
                ],
                "Недостатки": [
                    "Концентрация больных и персонала в одном здании.",
                    "Шумовое загрязнение и ухудшение микроклимата."
                ],
                "Description": "All departments (except infectious and pathology) in one building.",
                "Advantages": [
                    "Efficient use of beds and staff.",
                    "Reduced costs."
                ],
                "Disadvantages": [
                    "Concentration of patients and staff in one building.",
                    "Noise pollution and poor microclimate."
                ]
            },
            "Смешанная система": {
                "Описание": "Комбинация централизованных и децентрализованных элементов.",
                "Преимущества": [
                    "Оптимальное сочетание изоляции и централизации.",
                    "Удобство для пациентов и персонала."
                ],
                "Недостатки": [
                    "Сложность в планировании и строительстве."
                ],
                "Description": "Combination of centralized and decentralized elements.",
                "Advantages": [
                    "Optimal balance of isolation and centralization.",
                    "Convenience for patients and staff."
                ],
                "Disadvantages": [
                    "Complexity in planning and construction."
                ]
            },
            "Блочная система": {
                "Описание": "Отдельные блоки для разных отделений, соединенные переходами.",
                "Преимущества": [
                    "Централизация лечебно-диагностических служб.",
                    "Удобство перепланировки."
                ],
                "Недостатки": [
                    "Концентрация больных и персонала в вертикальных узлах.",
                    "Увеличение бактериальной загрязненности воздуха."
                ],
                "Description": "Separate blocks for different departments, connected by walkways.",
                "Advantages": [
                    "Centralization of diagnostic and treatment services.",
                    "Ease of reconfiguration."
                ],
                "Disadvantages": [
                    "Concentration of patients and staff in vertical nodes.",
                    "Increased bacterial contamination of air."
                ]
            }
        }

    def display_functional_zones(self):
        print("Functional Zones of Medical Facilities:")
        for zone_ru, zone_en in self.functional_zones.items():
            print(f"- {zone_ru} ({zone_en})")

    def display_zone_requirements(self):
        print("\nZone Requirements:")
        for zone, details in self.zone_requirements.items():
            print(f"{zone}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")

    def display_landscaping(self):
        print("\nLandscaping Requirements:")
        for requirement, details in self.landscaping.items():
            print(f"{requirement}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")

    def display_construction_systems(self):
        print("\nHospital Construction Systems:")
        for system, details in self.construction_systems.items():
            print(f"{system}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")
            print("  Преимущества:")
            for advantage in details["Преимущества"]:
                print(f"    - {advantage}")
            print("  Advantages:")
            for advantage in details["Advantages"]:
                print(f"    - {advantage}")
            print("  Недостатки:")
            for disadvantage in details["Недостатки"]:
                print(f"    - {disadvantage}")
            print("  Disadvantages:")
            for disadvantage in details["Disadvantages"]:
                print(f"    - {disadvantage}")


# Create an instance of the MedicalFacilityLayout class
hospital_layout = MedicalFacilityLayout()

# Display all information
hospital_layout.display_functional_zones()
hospital_layout.display_zone_requirements()
hospital_layout.display_landscaping()
hospital_layout.display_construction_systems()

class MedicalFacilityRequirements:
    def __init__(self):
        # Structural Units of a Hospital
        self.structural_units = {
            "Приемное отделение и помещения для выписки": "Admission and discharge departments",
            "Палатные отделения": "Ward departments",
            "Лечебно-диагностические отделения": "Diagnostic and treatment departments",
            "Лаборатории": "Laboratories",
            "Центральное стерилизационное отделение": "Central sterilization department",
            "Аптека": "Pharmacy",
            "Служба приготовления пищи": "Food service",
            "Патологоанатомическое отделение": "Pathology department",
            "Административно-хозяйственная служба": "Administrative and utility services",
            "Прачечная": "Laundry"
        }

        # Admission Department Requirements
        self.admission_department = {
            "Функции": {
                "Описание": "Регистрация, обследование, санитарная обработка пациентов.",
                "Description": "Registration, examination, and sanitary treatment of patients."
            },
            "Эпидемиологическая задача": {
                "Описание": "Не допустить поступления пациента с инфекционным заболеванием в общие палаты.",
                "Description": "Prevent patients with infectious diseases from entering general wards."
            },
            "Планировка": {
                "Описание": "Обеспечение поточности движения пациентов. Отдельные помещения для приема и выписки.",
                "Description": "Ensure smooth patient flow. Separate rooms for admission and discharge."
            }
        }

        # Ward Department Requirements
        self.ward_department = {
            "Секции": {
                "Описание": "Палатное отделение на 60 коек делится на две секции по 25-30 коек.",
                "Description": "A 60-bed ward department is divided into two sections of 25-30 beds each."
            },
            "Палаты": {
                "Описание": "Вместимость палат не должна превышать 4 койки. Рекомендуемая площадь: 10 м² на одного пациента в одноместных палатах, 7 м² для взрослых и 6 м² для детей в многоместных палатах.",
                "Description": "Ward capacity should not exceed 4 beds. Recommended area: 10 m² for single rooms, 7 m² for adults, and 6 m² for children in multi-bed rooms."
            },
            "Перевязочные": {
                "Описание": "В хирургических отделениях предусмотрены септические и асептические перевязочные.",
                "Description": "Surgical departments should have septic and aseptic dressing rooms."
            },
            "Изоляция": {
                "Описание": "Для пациентов с подозрением на инфекцию предусмотрены боксированные палаты.",
                "Description": "Isolation rooms are provided for patients suspected of having infections."
            }
        }

        # General Requirements
        self.general_requirements = {
            "Планировка": {
                "Описание": "Планировка должна исключать перекрещивание потоков с разной степенью эпидемиологической опасности.",
                "Description": "Layout should prevent cross-flows of different epidemiological risks."
            },
            "Помещения": {
                "Описание": "Помещения должны обеспечивать оптимальные условия для лечения, диагностики и труда персонала.",
                "Description": "Rooms should provide optimal conditions for treatment, diagnosis, and staff work."
            }
        }

    def display_structural_units(self):
        print("Structural Units of a Hospital:")
        for unit_ru, unit_en in self.structural_units.items():
            print(f"- {unit_ru} ({unit_en})")

    def display_admission_department(self):
        print("\nAdmission Department Requirements:")
        for category, details in self.admission_department.items():
            print(f"{category}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")

    def display_ward_department(self):
        print("\nWard Department Requirements:")
        for category, details in self.ward_department.items():
            print(f"{category}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")

    def display_general_requirements(self):
        print("\nGeneral Requirements for Medical Facilities:")
        for category, details in self.general_requirements.items():
            print(f"{category}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")


# Create an instance of the MedicalFacilityRequirements class
hospital_requirements = MedicalFacilityRequirements()

# Display all information
hospital_requirements.display_structural_units()
hospital_requirements.display_admission_department()
hospital_requirements.display_ward_department()
hospital_requirements.display_general_requirements()

class MedicalFacilityRequirements:
    def __init__(self):
        # Operating Block Requirements
        self.operating_block = {
            "Architectural Requirements": {
                "Описание": "Строгое соблюдение правил асептики, специализация операционных, удобства для персонала и пациентов.",
                "Description": "Strict adherence to aseptic rules, specialization of operating rooms, convenience for staff and patients."
            },
            "Zoning": {
                "Описание": "Операционный блок делится на стерильную зону, зону строгого режима и зону общебольничного режима.",
                "Description": "The operating block is divided into a sterile zone, a strict regime zone, and a general hospital zone."
            },
            "Ventilation": {
                "Описание": "Автономная система вентиляции с преобладанием притока воздуха в стерильных зонах.",
                "Description": "Autonomous ventilation system with predominant air supply in sterile zones."
            },
            "Sanitary Pass": {
                "Описание": "Персонал входит через санитарный пропускник, где проходит обработку и переодевание.",
                "Description": "Staff enters through a sanitary pass, where they undergo processing and change clothes."
            }
        }

        # Infectious Disease Departments
        self.infectious_departments = {
            "Layout": {
                "Описание": "Инфекционные отделения размещаются в отдельно стоящих зданиях с боксами и полубоксами.",
                "Description": "Infectious departments are located in separate buildings with boxes and semi-boxes."
            },
            "Boxes and Semi-Boxes": {
                "Описание": "Боксы и полубоксы изолируют пациентов, обеспечивая безопасность персонала.",
                "Description": "Boxes and semi-boxes isolate patients, ensuring staff safety."
            },
            "Ventilation": {
                "Описание": "В боксах и полубоксах устанавливается автономная вентиляция с преобладанием вытяжки.",
                "Description": "Autonomous ventilation with predominant exhaust is installed in boxes and semi-boxes."
            }
        }

        # Pediatric Departments
        self.pediatric_departments = {
            "Layout": {
                "Описание": "Детские отделения размещаются в изолированных секциях с отдельными входами.",
                "Description": "Pediatric departments are located in isolated sections with separate entrances."
            },
            "Rooms": {
                "Описание": "Палаты для детей до 3 лет должны быть со шлюзом, для детей старше 7 лет – не менее 20% коек со шлюзом.",
                "Description": "Rooms for children under 3 years old must have a sluice, for children over 7 years old – at least 20% of beds with a sluice."
            },
            "Infection Control": {
                "Описание": "Медицинский персонал должен носить маски и соблюдать правила гигиены.",
                "Description": "Medical staff must wear masks and follow hygiene rules."
            }
        }

        # Maternity Hospitals
        self.maternity_hospitals = {
            "Layout": {
                "Описание": "Родильные дома включают физиологическое, патологии беременности и обсервационное отделения.",
                "Description": "Maternity hospitals include physiological, pregnancy pathology, and observation departments."
            },
            "Delivery Rooms": {
                "Описание": "Родовые залы должны иметь автономную вентиляцию и зонирование.",
                "Description": "Delivery rooms must have autonomous ventilation and zoning."
            },
            "Postpartum Departments": {
                "Описание": "Послеродовые отделения организуются с раздельным или совместным пребыванием матери и ребенка.",
                "Description": "Postpartum departments are organized with separate or joint stay of mother and child."
            }
        }

    def display_operating_block(self):
        print("Operating Block Requirements:")
        for category, details in self.operating_block.items():
            print(f"{category}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")

    def display_infectious_departments(self):
        print("\nInfectious Disease Departments:")
        for category, details in self.infectious_departments.items():
            print(f"{category}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")

    def display_pediatric_departments(self):
        print("\nPediatric Departments:")
        for category, details in self.pediatric_departments.items():
            print(f"{category}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")

    def display_maternity_hospitals(self):
        print("\nMaternity Hospitals:")
        for category, details in self.maternity_hospitals.items():
            print(f"{category}:")
            print(f"  Описание: {details['Описание']}")
            print(f"  Description: {details['Description']}")


# Create an instance of the MedicalFacilityRequirements class
hospital_requirements = MedicalFacilityRequirements()

# Display all information
hospital_requirements.display_operating_block()
hospital_requirements.display_infectious_departments()
hospital_requirements.display_pediatric_departments()
hospital_requirements.display_maternity_hospitals()


