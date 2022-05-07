from pathlib import Path

# gensim monkeypatch
import collections.abc

collections.Mapping = collections.abc.Mapping

import gensim.models.keyedvectors as word2vec
import numpy as np

import sqlite3
import tqdm

from more_itertools import chunked

# vectors = str(Path(__file__).parent / "GoogleNews-vectors-negative300.bin")
# vectors = "nor-vectors.bin"
vectors = "nor-vectors-avis.bin"
model = word2vec.KeyedVectors.load_word2vec_format(vectors, binary=True, unicode_errors="replace")


con = sqlite3.connect("word2vec.db")
con.execute("PRAGMA journal_mode=WAL")
cur = con.cursor()
cur.execute("""create table if not exists word2vec (word text PRIMARY KEY, vec blob)""")
con.commit()


def bfloat(vec):
    """
    Half of each floating point vector happens to be zero in the Google model.
    Possibly using truncated float32 = bfloat. Discard to save space.
    """
    vec.dtype = np.int16
    return vec[1::2].tobytes()


# many weird words contain #, _ for multi-word
# some have e-mail addresses, start with numbers, :-), lots of === signs, ...

CHUNK_SIZE = 1111
con.execute("DELETE FROM word2vec")
with con:
    for words in chunked(tqdm.tqdm(model.index_to_key[:200000]), CHUNK_SIZE):
        con.executemany(
            "insert into word2vec values(?,?)",
            ((word, model[word].tobytes()) for word in words),
        )
