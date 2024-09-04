import unittest
from time_calculator import add_time

class TestTimeCalculator(unittest.TestCase):

    def test_same_period(self):
        self.assertEqual(add_time("3:00 PM", "3:10"), "6:10 PM")

    def test_am_to_pm(self):
        self.assertEqual(add_time("11:30 AM", "2:32"), "2:02 PM")

    def test_next_day(self):
        self.assertEqual(add_time("11:43 AM", "00:20"), "12:03 PM")
        self.assertEqual(add_time("10:10 PM", "3:30"), "1:40 AM (next day)")
        self.assertEqual(add_time("11:59 PM", "24:05"), "12:04 AM (2 days later)")
        self.assertEqual(add_time("8:16 PM", "466:02"), "6:18 AM (20 days later)")

    def test_with_weekday(self):
        self.assertEqual(add_time("3:00 PM", "3:10", "Tuesday"), "6:10 PM, Tuesday")
        self.assertEqual(add_time("11:30 AM", "2:32", "Monday"), "2:02 PM, Monday")
        self.assertEqual(add_time("11:43 AM", "00:20", "Friday"), "12:03 PM, Friday")
        self.assertEqual(add_time("10:10 PM", "3:30", "Friday"), "1:40 AM, Saturday")
        self.assertEqual(add_time("11:59 PM", "24:05", "Wednesday"), "12:04 AM, Friday")
        self.assertEqual(add_time("8:16 PM", "466:02", "Monday"), "6:18 AM, Sunday (20 days later)")

if __name__ == "__main__":
    unittest.main()
