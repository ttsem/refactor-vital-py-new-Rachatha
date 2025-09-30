from time import sleep
import sys
import math

class VitalSigns:
    title: str
    min_value: float
    max_value: float
    monitored_value: float

    def __init__(self, title: str, min_value: float = -math.inf, max_value: float = math.inf, monitored_value: float = 0.0):
        self.title = title
        self.min_value = min_value
        self.max_value = max_value
        self.monitored_value = monitored_value

    def mock_loading():
        for i in range(6):
            print('\r* ', end='')
            sys.stdout.flush()
            sleep(1)
            print('\r *', end='')
            sys.stdout.flush()
            sleep(1)

    def check_vital_sign(self) -> bool:
        if self.monitored_value < self.min_value or self.monitored_value > self.max_value:
            print(f'{self.title} is out of range!')
            self.mock_loading()
            return False
        return True