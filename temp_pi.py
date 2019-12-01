#importing os into our pyscript

import os

print("Yo mama this the temperature of yer cpu")

for cmd in range(6):
    cmd = 'cat /sys/class/thermal/thermal_zone0/temp'
    os.system(cmd)

print("there you go mutterficker")
