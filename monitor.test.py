import unittest
from .vital_signs import VitalSigns
from monitor import vitals_ok

import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):

    def test_VitalSigns_initialization(self):
        vital = VitalSigns('Test Vital', 10, 20, 15)
        self.assertEqual(vital.title, 'Test Vital')
        self.assertEqual(vital.min_value, 10)
        self.assertEqual(vital.max_value, 20)
        self.assertEqual(vital.monitored_value, 15)

    def test_VitalSigns_check_vital_sign(self):
        vital_in_range = VitalSigns('In Range', 10, 20, 15)
        self.assertTrue(vital_in_range.check_vital_sign())

        vital_out_of_range = VitalSigns('Out of Range', 10, 20, 25)
        self.assertFalse(vital_out_of_range.check_vital_sign())

    def test_vitals_ok(self):
        global temperature, pulseRate, spo2

        # Test case where all vitals are in range
        temperature = 98.6
        pulseRate = 75
        spo2 = 95
        self.assertTrue(vitals_ok(temperature=temperature, pulseRate=pulseRate, spo2=spo2))

        # Test case where temperature is out of range
        temperature = 105.0
        pulseRate = 75
        spo2 = 95
        self.assertFalse(vitals_ok())

        # Test case where pulse rate is out of range
        temperature = 98.6
        pulseRate = 50
        spo2 = 95
        self.assertFalse(vitals_ok())

        # Test case where SpO2 is out of range
        temperature = 98.6
        pulseRate = 75
        spo2 = 85
        self.assertFalse(vitals_ok())


if __name__ == '__main__':
  unittest.main()
