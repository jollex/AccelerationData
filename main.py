from adxl345 import ADXL345
from datetime import datetime
import sys, time, os

# Constants
INTERVAL = .1

# Check that we got the right number of arguments
if len(sys.argv) < 3:
	print "Usage: " + sys.argv[0] + " <# seconds to wait before running> <# seconds to run>"
	sys.exit(1)

# Parse arguments
wait_time = int(sys.argv[1])
run_time = int(sys.argv[2])

# Set up accelerometer
adxl345 = ADXL345()

# Wait for given amount of time
time.sleep(wait_time)

# Get current date and time to use as filename for recording data
file_name = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".csv"

# Get starting time
start_time = time.time()

# Open file for writing
with open(file_name, 'w') as data_file:
	# Run for length of time given
	while time.time() < start_time + run_time:
		# Get data from accelerometer
		axes = adxl345.getAxes(False) # True: g; False: m/s^2
		# Get current time
		current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
		# Format data from accelerometer
		data_line = ",%.3f,%.3f,%.3f\n" % (axes['x'], axes['y'], axes['z'])
		# Print data to stdout and write to file
		print current_time + data_line
		data_file.write(current_time + data_line)

		# Get data every tenth of a second
		time.sleep(INTERVAL)
