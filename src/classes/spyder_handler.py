from classes.spyder4dof import *

class SpyderHandler:
    def __init__(self, handler_):
        self.spyder_parts = []
        self.init_spyder()
        self.handler = handler_

    def init_spyder(self):
        self.spyder_parts.append(Spyder4dof(pin_=0, part_='2.2', min_=200, max_=600))
        self.spyder_parts.append(Spyder4dof(pin_=1, part_='2.3', min_=200, max_=700))
        self.spyder_parts.append(Spyder4dof(pin_=2, part_='2.1', min_=200, max_=600))
        self.spyder_parts.append(Spyder4dof(pin_=3, part_='--', min_=0, max_=0))
        self.spyder_parts.append(Spyder4dof(pin_=4, part_='1.3', min_=200, max_=700))
        self.spyder_parts.append(Spyder4dof(pin_=5, part_='1.1', min_=200, max_=600))
        self.spyder_parts.append(Spyder4dof(pin_=6, part_='1.2', min_=200, max_=600))
        self.spyder_parts.append(Spyder4dof(pin_=7, part_='5.1', min_=200, max_=1000))
        self.spyder_parts.append(Spyder4dof(pin_=8, part_='5.2', min_=200, max_=650))
        self.spyder_parts.append(Spyder4dof(pin_=9, part_='4.1', min_=200, max_=600))
        self.spyder_parts.append(Spyder4dof(pin_=10, part_='4.3', min_=200, max_=700))
        self.spyder_parts.append(Spyder4dof(pin_=11, part_='4.2', min_=200, max_=600))
        self.spyder_parts.append(Spyder4dof(pin_=12, part_='--', min_=0, max_=0))
        self.spyder_parts.append(Spyder4dof(pin_=13, part_='3.1', min_=250, max_=650))
        self.spyder_parts.append(Spyder4dof(pin_=14, part_='3.2', min_=200, max_=600))
        self.spyder_parts.append(Spyder4dof(pin_=15, part_='3.3', min_=200, max_=700))

    def move(self, part, position):
        '''Find part'''
        for tmp_part in self.spyder_parts:
            if tmp_part.part == part:
                tmp_part.move(self.handler, position)
                continue




