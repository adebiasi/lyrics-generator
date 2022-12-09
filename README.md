# lyrics-generator

## How to run the lyrics-generator

Run:

    py ./LyricsImporter.py
    
The main is:

```python
if __name__ == '__main__':

    lyrics_importer = LyricsImporter()
    lyrics_importer.create_markov_chain_dict_from_folder('./beatles_lyrics')
    lyrics_importer.create_lyrics()
```

## How it works

It applies the [n-gram](https://en.wikipedia.org/wiki/N-gram) model to a dataset of txt files.


## Some generated lyrics

Generated lyrics taking as input the entire production of Beatles songs (retrieved from https://github.com/tylerlewiscook/beatles-lyrics).

Here's one generated lyric:

    But they run, yeah-heh yeah yeah
    Look what you're gonna lose that went to me, hey hey bop shoo-wop
    Better, 'cause I'm kissing you
    Burns my blue suede shoes
    All together now
    Quiet!
    Baby, shake it too much, darling
    It's driving me a yellow submarine

Here's another one:

    Any old enough to heaven
    No, 'round
    All you
    All together now
    All together, I sat on, don't sound
    Oh, honey, and boy been alone
    Love you
    Yeah
