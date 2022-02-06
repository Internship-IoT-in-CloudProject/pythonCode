from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(0)
class Sensor:
    def temperature(self):
        temp = sense.get_temperature()
        print("Temperature: %s C" % temp)
        sense.show_message(f'Temperature: {round(temp)}c',text_colour=[0,255,0])

    def pressure(self):
        pressure = sense.get_pressure()
        print("Pressure: %s Millibars" % pressure)
        sense.show_message(f'Pressure: {round(pressure)}pa',text_colour=[255,0,0])

    def humidity(self):
        humidity = sense.get_humidity()
        print("Humidity: %s %%rH" % humidity)
        sense.show_message(f'Humidity: {round(humidity)}rh',text_colour=[0,0,255])


class GetData(Sensor):
     obj=Sensor()
     obj.temperature()
     obj.pressure()
     obj.humidity()
        
    
g=GetData()