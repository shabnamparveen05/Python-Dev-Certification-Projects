# Time Calculator

This project is a time calculator that adds a specified duration to a given start time. It calculates the resulting time and handles day changes and formatting. The tool also allows you to specify a starting day and will provide the resulting day of the week if the duration causes the time to roll over into the next day or beyond.

## Features

- **Add Time**: Adds a duration to a start time and calculates the resulting time.
- **Day Calculation**: Handles day changes if the duration extends beyond the current day.
- **Time Formatting**: Provides output in 12-hour clock format with AM/PM indicators.
- **Day of Week**: Optional feature to include the day of the week in the output.

## Functions

### `add_time(start, duration, d_day=None)`

Adds a specified duration to a given start time and returns the resulting time. Optionally, you can specify a starting day to get the resulting day of the week.

#### Parameters

- `start` (str): The start time in 12-hour format (e.g., "3:30 PM").
- `duration` (str): The duration to add in "hours:minutes" format (e.g., "2:12").
- `d_day` (str, optional): The starting day of the week (e.g., "Monday"). If provided, the function will include the resulting day of the week in the output.

#### Returns

- A string representing the resulting time in 12-hour format with AM/PM indicators. If `d_day` is provided, the day of the week will be included in the output.

#### Example Usage

```python
from time_calculator import add_time

print(add_time('3:30 PM', '2:12'))
# Output: '5:42 PM'

print(add_time('11:55 AM', '3:12'))
# Output: '3:07 PM'

print(add_time('2:59 AM', '24:00'))
# Output: '2:59 AM (next day)'

print(add_time('11:59 PM', '24:05'))
# Output: '12:04 AM (next day)'

print(add_time('8:16 PM', '466:02'))
# Output: '6:18 AM (2 days later)'

print(add_time('3:30 PM', '2:12', 'Monday'))
# Output: '5:42 PM, Monday'

print(add_time('2:59 AM', '24:00', 'Saturday'))
# Output: '2:59 AM, Sunday (next day)'

print(add_time('11:59 PM', '24:05', 'Wednesday'))
# Output: '12:04 AM, Thursday (next day)'

print(add_time('8:16 PM', '466:02', 'Tuesday'))
# Output: '6:18 AM, Thursday (2 days later)'
