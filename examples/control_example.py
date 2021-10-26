# pylint: disable=W0621
"""Asynchronous Python client for GLIMMR."""

import asyncio

from glimmr import Glimmr


async def main():
    """Show example on controlling your GLIMMR device."""
    async with Glimmr("192.168.1.34") as led:
        device = await led.update()
        print(device)
        print(device.version)
        device.device_mode = 0
        await led.set(device)
        await led.update()
        input("Press Enter to continue set device to ambient mode...")
        await led.ambient_scene(3)
        input("Press Enter to continue set device to solid ambient color...")
        await led.ambient_color("ff0000")
        input("Press Enter to turn device off...")
        device.device_mode = 0
        await led.set(device)
        await led.update()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
