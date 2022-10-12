import pytradfri
import argparse
import uuid

parser = argparse.ArgumentParser(
    description="Controller for the IKEA Tradfri exhibited at BEST 2022 by HTL Kaindorf"
)

parser.add_argument(
    "host",
    metavar="IP",
    type=str,
    help="IP of the Tradfri Gateway"
)

parser.add_argument(
    "key",
    metavar="XYZ",
    type=str,
    help="Security Code found on the bottom of the Tradfri device"
)

args = parser.parse_args()

if len(args.key) != 16:
    raise pytradfri.PytradfriError("Invalid Security Code length!")

identity = uuid.uuid4().hex
api_factory = pytradfri.api.libcoap_api.APIFactory(
    host=args.host,
    psk_id=identity
    )

try:
    psk = api_factory.generate_psk(args.key)
    print("Generated PSK: {}".format(psk))
except AttributeError as err:
    raise pytradfri.PytradfriError("Please provide the security code on the bottom of the Tradfri device as an argument") from err

api = api_factory.request

gateway = pytradfri.Gateway()

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