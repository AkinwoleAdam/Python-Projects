from datetime import datetime
import pytz

print(pytz.all_timezones)


newYorkTz = pytz.timezone("America/Los_Angeles")
lagos_tz = pytz.timezone('Africa/Lagos')

time_in_lagos = datetime.now(lagos_tz)
timeInNewYork = datetime.now(newYorkTz)

currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")
currentTimeInNewLagos = time_in_lagos.strftime("%H:%M:%S")

print(currentTimeInNewLagos)
print(currentTimeInNewYork)