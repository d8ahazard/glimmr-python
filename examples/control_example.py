# pylint: disable=W0621
"""Asynchronous Python client for GLIMMR."""

import asyncio

from glimmr import Glimmr


async def main():
    """Show example on controlling your GLIMMR device."""
    async with Glimmr("192.168.1.34") as led:
        await led.update()
        print(led.system_data)
        await led.set_mode(0)
        input("Press Enter to continue set device to ambient mode...")
        await led.set_ambient_scene(3)
        input("Press Enter to continue set device to solid ambient color...")
        await led.set_ambient_color("ff0000")
        input("Press Enter to turn device off...")
        await led.set_mode(0)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
