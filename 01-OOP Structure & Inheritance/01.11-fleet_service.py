#Focus: Class- vs Instance Attributes

class ElectricTruck:
    company_name = "LogiTrans"
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def show_info(self):
        return f"Truck {self.license_plate} belongs to {ElectricTruck.company_name}"

truck1 = ElectricTruck("FMD")
truck2 = ElectricTruck("DIN")

print(truck1.show_info())
print(truck2.show_info())

# Changes the name of the company
ElectricTruck.company_name = "GlobalLogistics"

print(truck1.show_info())
print(truck2.show_info())
