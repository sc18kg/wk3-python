class Car:
    def __init__(self, max):
        self.speed = 40
        self.max = max
    
    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed

    def accelerate(self, up):
        if self.speed < (self.max - up):
            self.speed += up
        else:
            self.speed = self.max
            print(f"You've reached the Limit of {self.max}! Cannot Go Faster!")
        # self.speed = min(self.max, self._speed + up)
    def decelerate(self, down):
        if (self.speed - down) > 0:
            self.speed -= down
        elif (self.speed - down) <= 0:
            self.speed = 0
            print(f"Car Stopped")
        # self.speed = max(0, self-speed - down)
    def getspeed(self):
        print(self.speed)

car = Car(100)

car.accelerate(67)
car.getspeed()


car.decelerate(40)
car.getspeed()
car.decelerate(70)
car.getspeed()

#if __name__ == "__main__":
#    do this code                A way to test where only if the file is the main is ran