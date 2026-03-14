class Robot:
    def __init__(self,name):
        self.name = name

    def start(self):
        print(self.name,"started")

    def stop(self):
        print(self.name,"stopped")


class HumanoidRobot(Robot):
    def speak(self):
        print(self.name,"is speaking")

    def start(self):  # method overriding
        print(self.name,"humanoid robot started with AI")


r = Robot("BasicBot")
r.start()
r.stop()

h = HumanoidRobot("AlphaBot")
h.start()
h.speak()
h.stop()