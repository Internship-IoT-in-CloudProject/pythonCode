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
    start=True
    while(start):
        print("what do you like to know\n1.Temperature - press T\n2.Pressure - press P\n3.Humidity - press H")
        d=input()
        obj=Sensor()
    
    
        if(d=="T" or d=="t"):
            obj.temperature()
        elif(d=="P" or d=="p"):
            obj.pressure()
        elif(d=="H" or d=="h"):
            obj.humidity()
        else:
            print("Do you want to exit? (y/n)")
            out=input()
            if(out=="y" or "yes"):
                exit()
        
        print("Do you want to continue? (y/n)")
        pursue=input()
        if(pursue=="n" or pursue=="no"):
            start=False
            exit()
    
g=GetData()
