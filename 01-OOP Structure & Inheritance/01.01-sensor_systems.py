class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self._battery_level = 100
        
    def __str__(self):
        return f"Sensor {self.sensor_id} - Battery: {self._battery_level}%"
    
    def calibrate(self):
        pass

sensor = Sensor("SN-99")
print(sensor)