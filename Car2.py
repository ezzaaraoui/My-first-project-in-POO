class Car:

    def __init__(self,speed,color,nitroSpeed,model):
        self.speed = speed
        self.color = color
        self.nitroSpeed = nitroSpeed
        self.model = model

    def turn(self):
        print("Car turn ")
    def accelerate(self):
        print("Car accelerating ")
    def brake(self):
        print("Car braking")
    def boost(self):
        print("Car boosting")
