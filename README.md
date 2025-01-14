# MaaJik / 孖翼

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/sammdot/plover-maajik)](https://github.com/sammdot/plover-maajik/releases/latest)
[![PyPI](https://img.shields.io/pypi/v/plover-maajik)](https://pypi.org/project/plover-maajik)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/sammdot/plover-maajik/build)
![GitHub](https://img.shields.io/github/license/sammdot/plover-maajik)

**WARNING: The information in this README may be inaccurate as this fork is different from the original repo.** 

MaaJik /ma˥ jɪk̚˨/ (孖翼, "a pair of wings") is a work-in-progress Cantonese
machine shorthand theory. This repository contains an implementation of it for
Plover, including a system plugin and dictionaries.

![MaaJik keyboard layout](https://raw.githubusercontent.com/sammdot/plover-maajik/main/assets/layout.png)

![MaaJik writing demo](https://raw.githubusercontent.com/sammdot/plover-maajik/main/assets/demo.png)

## Installation

1. Clone the repo onto your machine: `git clone https://github.com/vatnid/plover-maajik.git`
2. Navigate to the repo directory: `cd plover-maajik`
3. Run `plover -s plover_plugins install -e .` (remember the final dot!)
4. Restart Plover.
5. Go to `Configure > System`, and change your system to `MaaJik`.
6. You may need to add the default dictionaries manually.


## Usage

See the [documentation](https://github.com/sammdot/plover-maajik/blob/main/docs/README.md) included in this repository for a detailed explanation of how the MaaJik theory works.

The base dictionaries are in the `maajik/dictionaries` directory. Below is the recommended dictionary order:

- [`user.json`](https://github.com/sammdot/plover-maajik/blob/main/maajik/dictionaries/user.json) – Empty, add your own entries here
- [`commands.json`](https://github.com/sammdot/plover-maajik/blob/main/maajik/dictionaries/commands.json) – Formatting and control commands
- [`punctuation.json`](https://github.com/sammdot/plover-maajik/blob/main/maajik/dictionaries/punctuation.json) - Punctuation outlines
- [`briefs.json`](https://github.com/sammdot/plover-maajik/blob/main/maajik/dictionaries/briefs.json) – Briefs for common words and phrases
- [`cangjie.json`](https://github.com/sammdot/plover-maajik/blob/main/maajik/dictionaries/cangjie.json) – Cangjie fingerspelling entries
- _[`cangjie.py`](https://github.com/sammdot/plover-maajik/blob/main/maajik/dictionaries/cangjie.py)_ (_optional_, requires `plover-python-dictionary` plugin) – Visual indication of Cangjie code input
- [`base.json`](https://github.com/sammdot/plover-maajik/blob/main/maajik/dictionaries/base.json) – Phonetic entries

A Steno Explainers infographic of the basic phonetic chords is also available:

![MaaJik Steno Explainers](https://steno.sammdot.ca/maajik.png)
