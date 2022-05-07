"""
Dump vocabulary for hints.
"""
# gensim monkeypatch
import collections.abc

import typer
import gensim.models.keyedvectors as word2vec

def main(num_words: int=200000):
    vectors = "nor-vectors-avis.bin"
    model = word2vec.KeyedVectors.load_word2vec_format(vectors, binary=True, unicode_errors="replace")

    # TODO: filter punctuation - and/or use lemmatized vectors

    with open("words-104.txt", 'w') as f:
        for word in model.index_to_key[:num_words]:
            f.write(f"{word}\n")


if __name__ == '__main__':
    typer.run(main)
