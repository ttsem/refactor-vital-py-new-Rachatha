
import sys
import math
from .vital_signs import VitalSigns


def vitals_ok(temperature, pulseRate, spo2) -> bool:
    vital_signs_list = [
        VitalSigns('Temperature', temperature, 95.0, 104.0),
        VitalSigns('Pulse Rate', pulseRate, 60, 100),
        VitalSigns('SpO2', spo2, 0, 89)
    ]

    def check_all_vitals() -> bool:
        for vital in vital_signs_list:
            if not vital.check_vital_sign():
                return False
        return True
    
    return check_all_vitals()