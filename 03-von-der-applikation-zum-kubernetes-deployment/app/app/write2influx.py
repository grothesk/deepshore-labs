import math
import time
from influxdb import InfluxDBClient

from app.settings import INFLUX_HOST, INFLUX_PORT, DATABASE, MEASUREMENT


class TrigonometricsWriter:
    T_SLEEP = 1

    def __init__(self, logger):
        self.client = InfluxDBClient(
            host=INFLUX_HOST,
            port=INFLUX_PORT,
            database=DATABASE
        )
        self.logger = logger

    @staticmethod
    def omega(period_duration):
        return 2 * math.pi / period_duration

    def write(self, amplitude, period_duration, samples):
        w = self.omega(period_duration)
        for t in range(samples):
            points = [
                {
                    'measurement': MEASUREMENT,
                    'fields':
                        {
                            'sin': amplitude * math.sin(w * t),
                            'cos': amplitude * math.cos(w * t)
                        }
                }
            ]
            self.logger.info('Write sample to InfluxDB: %s', points)
            self.client.write_points(points)
            time.sleep(TrigonometricsWriter.T_SLEEP)
        self.logger.info('Done.')
