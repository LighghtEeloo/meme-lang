# Meme

A string template language hosted by Python3 runtime. Conventionally, the source code of this language is written in plain text with utf-8 encoding and stored in a file with extension ".meme".

## Philosophy

Human beings repeat one another, even themselves from time to time. Emerging from the dark flow of collective intelligence, memes are how we degenerated web inhabitants express our feelings, thoughts and our very existence. Yet, such expression is causing more and more brothers to suffer from language or behavioral disorders (e.g. little-pinky or vim-handicapped). The meme language is therefore introduced to DRY the web environment and encourage diversity across our mental homeland.

## Grammar

To keep the language implementation concise, the grammar of said language is aligned with the syntax described in [PEP 498](https://www.python.org/dev/peps/pep-0498/). 

Later you may find a detailed and formalized specification in `spec.pdf`, if the author (?) is charged up and functional.

## Installation

The language is based on [Python 3](https://www.python.org/), which can be installed [directly](https://www.python.org/downloads/) or via your system package manager. Make sure that you install a version that is superior than or equal to Python 3.6. Make sure that you also install [pip](https://pypi.org/project/pip/), the package manager for Python as well.

Then run

```bash
pip install --upgrade meme-lang
```

and meme-lang will be installed to your device.

## Usage

Using meme is easy.

```python
# import
from meme import Meme

# your meme template name
meme_name = ".meme"
# the contents to be filled into the meme template
meme_content = {}
# get the str of meme
meme = Meme(meme_name).print(**meme_content)

# output
print(meme)
```

You may also create various memes and collect them for future use.

## Disclaimer

This is merely a joke. Don’t take this seriously.
