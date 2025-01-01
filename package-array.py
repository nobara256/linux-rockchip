from json import loads, dumps
from sys import argv
from datetime import datetime


payload = loads(argv[1])


def kernel_ver_selector(package):
    return (
        package["moniker"] == "mainline" or
        package["version"] == payload["latest_stable"]["version"]
    )

print(dumps({"array": list(filter(kernel_ver_selector, payload["releases"]))}, indent=None))


