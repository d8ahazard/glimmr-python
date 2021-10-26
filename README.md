# Python: GLIMMR API Client

[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE.md)

[![Build Status][build-shield]][build]
[![Code Coverage][codecov-shield]][codecov]
[![Code Quality][code-quality-shield]][code-quality]
[![Deepcode.ai][deepcode-shield]][deepcode]

[![Sponsor D8ahazard via GitHub Sponsors][github-sponsors-shield]][github-sponsors]

[![Support D8ahazard on Patreon][patreon-shield]][patreon]

Asynchronous Python client for Glimmr.

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

from glimmr import GLIMMR


async def main():
    """Show example on controlling your GLIMMR device."""
    async with GLIMMR("glimmr-d8ahazard.local") as led:
        device = await led.update()
        print(device.info.version)

        # Turn strip on, full brightness
        await led.light(on=True, brightness=255)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

## Changelog & Releases

This repository keeps a change log using [GitHub's releases][releases]
functionality.

Releases are based on [Semantic Versioning][semver], and use the format
of `MAJOR.MINOR.PATCH`. In a nutshell, the version will be incremented
based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

This Python project is fully managed using the [Poetry][poetry] dependency
manager. But also relies on the use of NodeJS for certain checks during
development.

You need at least:

- Python 3.8+
- [Poetry][poetry-install]
- NodeJS 12+ (including NPM)

To install all packages, including all development requirements:

```bash
npm install
poetry install
```

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

## Authors & contributors

The original setup of this repository is by [Franck Nijhof][d8ahazard].

For a full list of all authors and contributors,
check [the contributor's page][contributors].

## License

MIT License

Copyright (c) 2019-2021 Franck Nijhof

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[build-shield]: https://github.com/d8ahazard/python-glimmr/actions/workflows/tests.yaml/badge.svg
[build]: https://github.com/d8ahazard/python-glimmr/actions/workflows/tests.yaml
[code-quality-shield]: https://img.shields.io/lgtm/grade/python/g/d8ahazard/python-glimmr.svg?logo=lgtm&logoWidth=18
[code-quality]: https://lgtm.com/projects/g/d8ahazard/python-glimmr/context:python
[codecov-shield]: https://codecov.io/gh/d8ahazard/python-glimmr/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/d8ahazard/python-glimmr
[contributors]: https://github.com/d8ahazard/python-glimmr/graphs/contributors
[deepcode-shield]: https://www.deepcode.ai/api/gh/badge?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybTEiOiJnaCIsIm93bmVyMSI6ImZyZW5jayIsInJlcG8xIjoicHl0aG9uLWVsZ2F0byIsImluY2x1ZGVMaW50IjpmYWxzZSwiYXV0aG9ySWQiOjI4MDU1LCJpYXQiOjE2MTUxODgzODh9.hJsD6PTw8K8bnTmHUzroQi7XkXRi46bdt-oMqx2zXj0
[deepcode]: https://www.deepcode.ai/app/gh/d8ahazard/python-glimmr/_/dashboard?utm_content=gh%2Fd8ahazard%2Fpython-glimmr
[d8ahazard]: https://github.com/d8ahazard
[github-sponsors-shield]: https://d8ahazard.dev/wp-content/uploads/2019/12/github_sponsor.png
[github-sponsors]: https://github.com/sponsors/d8ahazard
[license-shield]: https://img.shields.io/github/license/d8ahazard/python-glimmr.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2021.svg
[patreon-shield]: https://d8ahazard.dev/wp-content/uploads/2019/12/patreon.png
[patreon]: https://www.patreon.com/d8ahazard
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com/
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/glimmr/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/glimmr
[releases-shield]: https://img.shields.io/github/release/d8ahazard/python-glimmr.svg
[releases]: https://github.com/d8ahazard/python-glimmr/releases
[semver]: http://semver.org/spec/v2.0.0.html
