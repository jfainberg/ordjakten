# Ordjakten

This is a Norwegian version of David Turner's [Semantle](https://www.semantle.com), heavily based on the original source code.

## Running

So, this is sort of hacked together from a lot of data sources and the
code is a mess.  Here's a hello world of how to get up and running.

1. Install Python requirements using `pip install -r requirements.txt`.

2. Download `GoogleNews-vectors-negative300.bin.gz` from [here](https://code.google.com/archive/p/word2vec/), and extract it into the parent directory of this project.

3. Run `python dump-vecs.py` to create an SQLite database and store the main vectors.

4. Run `python dump-hints.py` to create a hints pickle. Wait a very long time.

5. Run `python store-hints.py` to import the pickle into the DB.

6. Run `python semantle.py` for the web server.

## Development

Install the pre-commit to run black, isort and flake8.
