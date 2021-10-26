# pylint: disable=W0621
"""Asynchronous Python client for GLIMMR."""

import asyncio

from glimmr import Glimmr, SystemData


async def main():
    """Show example on WebSocket usage with GLIMMR."""
    async with Glimmr("192.168.1.34") as led:
        await led.connect()
        if led.connected:
            print("connected!")

        def something_updated(device) -> None:
            """Call when GLIMMR reports a state change."""  # noqa
            print("Received an update from GLIMMR")
            print(device.version)
            print(device.device_name)

        # Start listening
        led.add_callback("olo", something_updated)

        # Now we wait...
        await asyncio.sleep(3600)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
