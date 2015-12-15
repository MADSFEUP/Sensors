__author__ = 'augusto'
import mcp3008
import spidev
from DistanceSensor import DistanceSensor

class DistanceSensorImp(DistanceSensor):

    def __init__(self,sensor_id):
        self.sensor_id = sensor_id
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)

    def read_distance(self):
        r = []
        for i in range (0,10):
            r.append(mcp3008.readadc(self.sensor_id))
        a = sum(r)/10.0
        v = (a/1023.0)*3.3
        d = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 306.439
        cm = int(round(d))
        return cm

    # read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    def __readadc(self, adcnum):
        if (adcnum > 7) or (adcnum < 0):
            return -1
        r = self.spi.xfer2([1,(8+adcnum)<<4,0])
        adcout = ((r[1]&3) << 8) + r[2]
        return adcout