print ("i am a new creature!\ni can do many things but i still do not have a body.")

print("my first task is to tell you how to build a hospital!")

class InfectiousHospitalLayout:
    def __init__(self, total_area):
        self.total_area = total_area
        self.zones = {
            "infectious_zone": 0,
            "green_belt": 0,
            "decontamination_area": 0,
            "housing_zone": 0,
            "container_platform": 0
        }

    def add_zone(self, zone_name, area):
        if zone_name in self.zones:
            self.zones[zone_name] += area
        else:
            raise ValueError(f"Unknown zone: {zone_name}")

    def check_layout(self):
        # Check if the total area is within the specified limits
        total_used_area = sum(self.zones.values())
        if total_used_area > self.total_area:
            return False, "Total used area exceeds the total area of the plot."

        # Check if the infectious zone is isolated by a green belt
        if self.zones["infectious_zone"] > 0 and self.zones["green_belt"] == 0:
            return False, "Infectious zone should be isolated by a green belt."

        # Check if the container platform is correctly sized
        if self.zones["container_platform"] > 0:
            container_base_area = self.zones["container_platform"] - 1.5 * 4  # Assuming square containers
            if container_base_area < 0:
                return False, "Container platform size is incorrect."

        return True, "Layout is compliant with the guidelines."

    def display_layout(self):
        for zone, area in self.zones.items():
            print(f"{zone}: {area} square meters")

class HospitalConstructionSystem:
    def __init__(self, system_type):
        self.system_type = system_type

    def describe_system(self):
        if self.system_type == "centralized":
            return (
                "Centralized system: All subdivisions of the hospital are located in one multi-story building "
                "(except for the infectious ward).\n"
                "Disadvantage: Concentration of a large number of patients and staff on a limited territory "
                "of a multi-story building."
            )
        elif self.system_type == "decentralized":
            return (
                "Decentralized (pavilion) system: Hospital departments, usually of the same profile, are located "
                "in low-rise buildings (1-3 floors).\n"
                "Advantages: Separation of different groups of patients (infectious, psychiatric, pediatric, etc.).\n"
                "Disadvantages: Requires large areas for the placement of hospital subdivisions."
            )
        elif self.system_type == "mixed":
            return (
                "Mixed system: The main somatic departments along with auxiliary services are located in a multi-story "
                "building, while departments requiring separation (maternity, pediatric, infectious, etc.) are in "
                "separate buildings. All departments are connected by underground passages.\n"
                "Common diagnostic department."
            )
        else:
            return "Unknown system type."
        
        
def calculate_polyclinic_size(visits_per_shift):
    """
    Calculate the required land area for a polyclinic.

    Parameters:
    visits_per_shift (int): Number of visits per shift.

    Returns:
    float: Required land area in hectares.
    """
    # 0.1 hectares per 100 visits per shift, but not less than 0.5 hectares
    required_land = max(0.1 * (visits_per_shift / 100), 0.5)
    return required_land

def calculate_pharmacy_size():
    """
    Calculate the required land area for a pharmacy.

    Returns:
    tuple: Minimum and maximum required land area in hectares.
    """
    # 0.2 to 0.4 hectares per facility
    return 0.2, 0.4

def calculate_emergency_station_size():
    """
    Calculate the required land area for an emergency medical station.

    Returns:
    tuple: Minimum and maximum required land area in hectares.
    """
    # 0.2 to 0.4 hectares per facility
    return 0.2, 0.4

def calculate_nursing_home_size(num_beds):
    """
    Calculate the required land area for a nursing home.

    Parameters:
    num_beds (int): Number of beds in the nursing home.

    Returns:
    tuple: Minimum and maximum required land area in square meters.
    """
    # 80 to 100 square meters per bed
    min_area = num_beds * 80
    max_area = num_beds * 100
    return min_area, max_area

def calculate_hospital_plot_size(num_beds):
    """
    Calculate the required plot size for a hospital based on the number of beds.

    Parameters:
    num_beds (int): Number of beds in the hospital.

    Returns:
    int: Required plot size in square meters.
    """
    if num_beds <= 60:
        plot_size_per_bed = 300
    elif 61 <= num_beds <= 200:
        plot_size_per_bed = 200
    elif 201 <= num_beds <= 500:
        plot_size_per_bed = 150
    elif 501 <= num_beds <= 700:
        plot_size_per_bed = 100
    elif 701 <= num_beds <= 900:
        plot_size_per_bed = 80
    else:  # num_beds >= 901
        plot_size_per_bed = 60

    total_plot_size = num_beds * plot_size_per_bed
    return total_plot_size

def calculate_land_usage(total_area):
    """
    Calculate the required areas for green spaces and construction based on the total area.

    Parameters:
    total_area (float): Total area of the plot in square meters.

    Returns:
    dict: A dictionary containing the areas for green spaces and construction.
    
    """
    
    
    
    # Calculate the minimum area for green spaces (50% of total area)
    green_spaces_area = total_area * 0.5

    # Calculate the maximum area for construction (15% of total area)
    construction_area = total_area * 0.15

    return {
        "green_spaces_area": green_spaces_area,
        "construction_area": construction_area
    }

def check_tree_and_shrub_placement(building_dimensions, tree_distance, shrub_distance):
    """
    Check the placement of trees and shrubs around the building.

    Parameters:
    building_dimensions (tuple): Dimensions of the building (length, width) in meters.
    tree_distance (float): Minimum distance from the building for trees in meters.
    shrub_distance (float): Minimum distance from the building for shrubs in meters.

    Returns:
    bool: True if the placement is compliant, False otherwise.
    """
    length, width = building_dimensions

    # Check if the trees are placed at least 15 meters away from the building
    if tree_distance < 15:
        return False

    # Check if the shrubs are placed at least 5 meters away from the building
    if shrub_distance < 5:
        return False

    return True

def check_window_placement(building_dimensions, window_distance):
    """
    Check the placement of windows and other critical areas.

    Parameters:
    building_dimensions (tuple): Dimensions of the building (length, width) in meters.
    window_distance (float): Minimum distance from the building for windows in meters.

    Returns:
    bool: True if the placement is compliant, False otherwise.
    """
    length, width = building_dimensions

    # Check if the windows are placed at least the specified distance away from the building
    if window_distance < 5:
        return False

    return True

class HospitalLayout:
    def __init__(self, total_area):
        self.total_area = total_area
        self.zones = {
            "lechebnye_korpusa": 0,
            "pediatriya": 0,
            "psihosomatika": 0,
            "kozhno_venerologiya": 0,
            "radiologiya": 0,
            "roddom": 0,
            "sadovo_parkovaya": 0,
            "poliklinika": 0,
            "patologoanatomiya": 0,
            "hoz_sooruzheniya": 0
        }

    def add_zone(self, zone_name, area):
        if zone_name in self.zones:
            self.zones[zone_name] += area
        else:
            raise ValueError(f"Unknown zone: {zone_name}")

    def check_layout(self):
        # Check if the total area is within the specified limits
        total_used_area = sum(self.zones.values())
        if total_used_area > self.total_area:
            return False, "Total used area exceeds the total area of the plot."

        # Check if the patologoanatomiya is isolated
        if self.zones["patologoanatomiya"] > 0:
            if self.zones["lechebnye_korpusa"] > 0 or self.zones["roddom"] > 0:
                return False, "Patologoanatomiya should be isolated from lechebnye_korpusa and roddom."

        return True, "Layout is compliant with the guidelines."

    def display_layout(self):
        for zone, area in self.zones.items():
            print(f"{zone}: {area} square meters")

# Example usage
if __name__ == "__main__":
    # Polyclinic example
    visits_per_shift = 250
    polyclinic_size = calculate_polyclinic_size(visits_per_shift)
    print(f"Polyclinic size for {visits_per_shift} visits per shift: {polyclinic_size} hectares")

    # Pharmacy example
    pharmacy_size_min, pharmacy_size_max = calculate_pharmacy_size()
    print(f"Pharmacy size: {pharmacy_size_min} to {pharmacy_size_max} hectares")

    # Emergency Medical Station example
    emergency_station_size_min, emergency_station_size_max = calculate_emergency_station_size()
    print(f"Emergency Medical Station size: {emergency_station_size_min} to {emergency_station_size_max} hectares")

    # Nursing Home example
    num_beds = 50
    nursing_home_size_min, nursing_home_size_max = calculate_nursing_home_size(num_beds)
    print(f"Nursing Home size for {num_beds} beds: {nursing_home_size_min} to {nursing_home_size_max} square meters")
    
    # Example number of beds
    num_beds = 300
    plot_size = calculate_hospital_plot_size(num_beds)
    print(f"For {num_beds} beds, the required hospital plot size is {plot_size} square meters.")

    # Additional examples
    examples = [50, 150, 350, 600, 800, 1000]
    for beds in examples:
       plot_size = calculate_hospital_plot_size(beds)
       print(f"For {beds} beds, the required hospital plot size is {plot_size} square meters.")
       
    # Total area of the plot
    total_area = 10000  # in square meters

    # Calculate the required areas
    land_usage = calculate_land_usage(total_area)
    print(f"Total area: {total_area} square meters")
    print(f"Green spaces area: {land_usage['green_spaces_area']} square meters")
    print(f"Construction area: {land_usage['construction_area']} square meters")

    # Building dimensions
    building_dimensions = (50, 30)  # length and width in meters

    # Check tree and shrub placement
    tree_distance = 20  # in meters
    shrub_distance = 6  # in meters
    is_compliant_trees_shrubs = check_tree_and_shrub_placement(building_dimensions, tree_distance, shrub_distance)
    print(f"Tree and shrub placement compliant: {is_compliant_trees_shrubs}")

    # Check window placement
    window_distance = 7  # in meters
    is_compliant_windows = check_window_placement(building_dimensions, window_distance)
    print(f"Window placement compliant: {is_compliant_windows}")
    
    # Total area of the hospital plot
    total_area = 50000  # in square meters

   # Create a hospital layout object
    hospital_layout = HospitalLayout(total_area)

   # Add zones with their respective areas
    hospital_layout.add_zone("lechebnye_korpusa", 10000)
    hospital_layout.add_zone("pediatriya", 5000)
    hospital_layout.add_zone("psihosomatika", 3000)
    hospital_layout.add_zone("kozhno_venerologiya", 2000)
    hospital_layout.add_zone("radiologiya", 4000)
    hospital_layout.add_zone("roddom", 6000)
    hospital_layout.add_zone("sadovo_parkovaya", 10000)
    hospital_layout.add_zone("poliklinika", 5000)
    hospital_layout.add_zone("patologoanatomiya", 2000)
    hospital_layout.add_zone("hoz_sooruzheniya", 3000)

   # Display the layout
    hospital_layout.display_layout()

   # Check the layout compliance
    is_compliant, message = hospital_layout.check_layout()
    print(f"Layout compliance: {is_compliant}")
    print(f"Message: {message}")
    
    # Example usage
if __name__ == "__main__":
    # Total area of the hospital plot
    total_area = 100000  # in square meters

    # Create an infectious hospital layout object
    infectious_hospital_layout = InfectiousHospitalLayout(total_area)

    # Add zones with their respective areas
    infectious_hospital_layout.add_zone("infectious_zone", 15000)
    infectious_hospital_layout.add_zone("green_belt", 5000)
    infectious_hospital_layout.add_zone("decontamination_area", 1000)
    infectious_hospital_layout.add_zone("housing_zone", 20000)
    infectious_hospital_layout.add_zone("container_platform", 500)

    # Display the layout
    infectious_hospital_layout.display_layout()

    # Check the layout compliance
    is_compliant, message = infectious_hospital_layout.check_layout()
    print(f"Layout compliance: {is_compliant}")
    print(f"Message: {message}")

    # Describe different hospital construction systems
    centralized_system = HospitalConstructionSystem("centralized")
    decentralized_system = HospitalConstructionSystem("decentralized")
    mixed_system = HospitalConstructionSystem("mixed")

    print("\nCentralized System:")
    print(centralized_system.describe_system())

    print("\nDecentralized System:")
    print(decentralized_system.describe_system())

    print("\nMixed System:")