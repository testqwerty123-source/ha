class Appliance:
    def __init__(self, brand, model, power_consumption):
        self.brand = brand
        self.model = model
        self.power_consumption = power_consumption
        self._is_on = False

    def turn_on(self):
        if not self._is_on:
            self._is_on = True

    def turn_off(self):
        if self._is_on:
            self._is_on = False

    def get_status(self):
        status = "увімкнено" if self._is_on else "вимкнено"
        return f"{self.brand} {self.model}: {status}"

class WashingMachine(Appliance):
    def __init__(self, brand, model, power_consumption, capacity_kg, spin_speed):
        super().__init__(brand, model, power_consumption)
        self.capacity_kg = capacity_kg
        self.spin_speed = spin_speed
        self._current_program = "Standby"

    def select_program(self, program_name):
        if self._is_on:
            self._current_program = program_name

    def start_wash(self):
        if self._is_on and self._current_program != "Standby":
            pass

    def get_status(self):
        base_status = super().get_status()
        return f"{base_status}, Об'єм: {self.capacity_kg} кг, Програма: {self._current_program}"

class Refrigerator(Appliance):
    def __init__(self, brand, model, power_consumption, freezer_capacity_l, fridge_temp_c, freezer_temp_c):
        super().__init__(brand, model, power_consumption)
        self.freezer_capacity_l = freezer_capacity_l
        self.fridge_temp_c = fridge_temp_c
        self.freezer_temp_c = freezer_temp_c

    def set_temperature(self, fridge_temp, freezer_temp):
        if self._is_on:
            self.fridge_temp_c = fridge_temp
            self.freezer_temp_c = freezer_temp

    def get_status(self):
        base_status = super().get_status()
        return f"{base_status}, Хол. {self.fridge_temp_c}°C, Мороз. {self.freezer_temp_c}°C"


my_washer = WashingMachine(brand="Bosh", model="Series 6", power_consumption=2200, capacity_kg=9.0, spin_speed=1400)
my_washer.turn_on()
my_washer.select_program("Eco")

my_fridge = Refrigerator(brand="LG", model="No Frost", power_consumption=180, freezer_capacity_l=100, fridge_temp_c=5, freezer_temp_c=-18)
my_fridge.turn_on()
my_fridge.set_temperature(fridge_temp=2, freezer_temp=-20)


print(my_washer.get_status())
print(my_fridge.get_status())
