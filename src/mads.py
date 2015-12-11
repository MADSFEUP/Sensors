import mcp3008
 
def write_distance():
	r = []
	for i in range (0,10):
		r.append(mcp3008.readadc(1))
	a = sum(r)/10.0
	v = (a/1023.0)*3.3
	d = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 306.439
	cm = int(round(d))
	val = '%d cm' % cm

  
import spidev
	spi = spidev.SpiDev()
	spi.open(0,0)
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
	def readadc(adcnum):
	if ((adcnum > 7) or (adcnum < 0)):
		return -1
	r = spi.xfer2([1,(8+adcnum)<<4,0])
	adcout = ((r[1]&3) << 8) + r[2]
	return adcout

'''
1. mkdir python-spi
2. cd python-spi
3. wget https://raw.github.com/doceme/py-spidev/master/setup.py
4. wget https://raw.github.com/doceme/py-spidev/master/spidev_module.c sudo python setup.py install

MCP3008 - 8-Channel 10-Bit ADC With SPI Interface ID: 856 - $3.75 : Adafruit Industries, Unique & fun DIY electronics and kits

Connecting the Cobbler to a MCP3008 | Analog Inputs for Raspberry Pi Using the MCP3008 | Adafruit Learning System

Overview | Analog Inputs for Raspberry Pi Using the MCP3008 | Adafruit Learning System

Arduino Blag: Long Range Infrared Sensor: GP2Y0A02YK0F

Jeremy's Blog: Raspberry Pi hardware SPI analog inputs using the MCP3008

Analogue Sensors On The Raspberry Pi Using An MCP3008

Jeremy's Blog: Raspberry Pi distance measuring sensor with LCD output

GPIO: Raspberry Pi Models A and B - Raspberry Pi Documentation

GPIO: Raspberry Pi Models A and B - Raspberry Pi Documentation

Enabling The SPI Interface On The Raspberry Pi

Raspberry Pi • View topic - GPIO instructions in MagPi result in error (solved)

'''

