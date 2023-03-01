class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.med = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        self.carType = carType
        if (self.carType == 1 and self.big == 0) or (self.carType == 2 and self.med == 0) or (
                self.carType == 3 and self.small == 0):
            return False
        if (self.carType == 1):
            self.big -= 1
        if (self.carType == 2):
            self.med -= 1
        if (self.carType == 3):
            self.small -= 1
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
