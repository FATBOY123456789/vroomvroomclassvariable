class Vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage
V1=Vehicle(maxspeed=250,mileage=10)
print('Vehicles max speed is: ',V1.maxspeed,'and vehicles mileage is: ',V1.mileage)