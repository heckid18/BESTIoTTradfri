import time
from tradfri import tradfriActions
hubip='192.168.1.109'
securityid='Zl5EvN4H4u75p77a'
bulbid='65537'

state = 0

def switch_on(hubip, securityid, bulbid):
    tradfriActions.tradfri_power_light(hubip, securityid, bulbid, 'on')
    print('Lights switched on!')

def switch_off(hubip, securityid, bulbid):
    tradfriActions.tradfri_power_light(hubip, securityid, bulbid, 'off')
    print('Lights switched off!')

switch_off(hubip, securityid, bulbid)


