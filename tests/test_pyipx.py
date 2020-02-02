import time
import sys
sys.path.append("/home/homeassistant/hass.dev/homeassistant/lib/python3.6/site-packages")

from pyipx800 import pyipx800

# Setup IPX800 V4
ipx = pyipx800.pyipx800("192.168.1.106", 80, "apikey")
ipx.configure()

d1 = ipx.inputs[0]
print("Input %d : <%s> = %d" % (d1.id, d1.name, d1.state))

a1 = ipx.analogs[0]
print("Analog %d : <%s> = %d" % (a1.id, a1.name, a1.state))

r1 = ipx.relays[0]
#r1.on() # Turn on the relay
print("Relay %d : <%s> = %d" % (r1.id, r1.name, r1.state))
time.sleep(2) # Wait 2 seconds
r1.off() # Turn off the relay 
print("Relay %d : <%s> = %d" % (r1.id, r1.name, r1.state))

c1 = ipx.counters[0]
i=1
while i<10:
  print("Counter %d : <%s> = %d" % (c1.id, c1.name, c1.state))
  time.sleep(1)
  i = i + 1

vi = ipx.virt_inputs[0]
vi.on()

vo=ipx.virt_outputs[0]
vo.on()

va=ipx.virt_analogs[0]
va.set(10)
