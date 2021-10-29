# pylint: disable=W0621
"""Asynchronous Python client for GLIMMR."""

import asyncio
import logging
import sys

from glimmr import Glimmr

logging.getLogger().addHandler(logging.StreamHandler())
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


async def main():
    """Show example on WebSocket usage with GLIMMR."""
    async with Glimmr("192.168.1.34") as led:
        led.LOGGER = logging
        led.socket.start()
        # Start listening

        def something_updated(data):
            """Call when GLIMMR reports a state change."""  # noqa
            print("Received an update from glimmr: %s", data[0]["systemData"])

        led.socket.on("olo", something_updated)
        if led.connected:
            print("connected!")

        # Now we wait...
        await asyncio.sleep(3600)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
