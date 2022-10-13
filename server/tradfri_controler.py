from pytradfri import Gateway
from pytradfri.api.libcoap_api import APIFactory
from pytradfri.error import PytradfriError
import sys
import uuid
IP="192.168.1.109"
KEY="Zl5EvN4H4u75p77a"

if len(KEY) != 16:
    raise PytradfriError("Invalid Security Code length!")

identity = uuid.uuid4().hex
api_factory = APIFactory(
    host=IP,
    psk_id=identity
    )

try:
    psk = api_factory.generate_psk(KEY)
    print("Generated PSK: {}".format(psk))
except AttributeError as err:
    raise PytradfriError("Please provide the security code on the bottom of the Tradfri device as an argument") from err

api = api_factory.request

gateway = Gateway()

devices = api(api(gateway.get_devices()))

def findTradfriLights():
    print("Printing information about all lamps paired to the Gateway")
    lights = [dev for dev in devices if dev.has_light_control]
    if not lights:
        sys.exit(bold("No lamps paired"))

    container: list[dict[str, Any]] = []
    for light in lights:
        container.append(light.raw.dict())
    print(jsonify(container))
    return container

def changeLightBrighteness(light, brighteness):
    light.light_controll.set_dimmer(brighteness)

changeLightBrighteness(findTradfriLights()[0], 50)