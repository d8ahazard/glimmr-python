# Python Glimmr API Client

An asynchronous Python client for Glimmr.

## About

This package allows you to control and monitor a Glimmr device
programmatically. It is mainly created to allow third-party programs to automate
the behavior of Glimmr.

## Installation

```bash
pip install glimmr
```

## Usage

```python
import asyncio
from glimmr import Glimmr

async def main():
    """Show example on controlling your GLIMMR device."""
    async with Glimmr("glimmr-333.local") as led:
        device = await led.update()
        print(device.info.version)
        # Add callback for data from web socket
        led.add_callback("olo", data_updated)

        # Set device to video mode
        await led.mode(1)
        await asyncio.sleep(1000)
        # Ambient color
        await led.ambient_color("FF00FF")
        await asyncio.sleep(1000)
        # Ambient scene
        await led.ambient_scene(4)
        await asyncio.sleep(1000)
        # Set device to "off"
        await led.mode(0)

def data_updated(self, data):
    print("Websocket callback: ", data)
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.