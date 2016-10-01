class Spyder4dof:
    def __init__(self, pin_, part_, min_, max_):
        self.pin = pin_
        self.part = part_
        self.min = min_
        self.max = max_
        self.max_percentage = 100
        self.k = 0.0
        self.pwm_value = 0.0

    def move(self, handler, position):
        """
        Move part to specific position (0 - 100) percentage
        :param handler: i2c Adafruit servo controller
        :param position: 0 - 100 %
        :return:
        """
        if position <=0:
            position = 0.001

        if position > self.max_percentage:
            position = self.max_percentage

        self.k = (self.max - self.min) / self.max_percentage
        self.pwm_value = self.min + (self.k * position)
        handler.set_pwm(self.pin, 0, int(self.pwm_value) )


