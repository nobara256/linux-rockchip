from json import loads, dumps
from sys import argv
from datetime import datetime


payload = loads(argv[1])


package_done_already = {}


def kernel_ver_selector(package):
    return (
        (package["moniker"] == "mainline" or package["moniker"] == "stable") and
        (package["version"] not in package_done_already)
    )


payload_array = list(filter(kernel_ver_selector, payload["releases"]))


print(
    "array="+dumps({"include": payload_array},
    indent=None
    ),
    end=""
)


