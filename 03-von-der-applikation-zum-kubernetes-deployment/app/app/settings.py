import os

INFLUX_HOST = os.getenv('INFLUX_HOST', 'localhost')
INFLUX_PORT = os.getenv('INFLUX_PORT', 8086)
DATABASE = os.getenv('INFLUXDB_DB', 'deeptalk')
MEASUREMENT = os.getenv('MEASUREMENT', 'signals')
