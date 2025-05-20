# Lyrics Generator

## Overview

This project uses a Markov chain approach based on the [n-gram](https://en.wikipedia.org/wiki/N-gram) model to generate song lyrics. The dataset consists of plain text files, and the generator creates new lyrics that mimic the style of the input text.

## How to Run

To run the lyrics generator, execute the following command:
```bash
py ./LyricsImporter.py
```
The entry point of the program is:

```python
if __name__ == '__main__':
    lyrics_importer = LyricsImporter()
    lyrics_importer.create_markov_chain_dict_from_folder('./beatles_lyrics')
    lyrics_importer.create_lyrics()
```

## How It Works

1. Loads all `.txt` files from the specified folder.
2. Builds a Markov chain dictionary based on n-grams.
3. Generates lyrics by probabilistically chaining words together.

The model captures local word dependencies, allowing it to produce text that resembles the input style.

## Example Generated Lyrics

Using the complete collection of Beatles lyrics (sourced from [this repository](https://github.com/tylerlewiscook/beatles-lyrics)), here are a few examples of generated lyrics:

**Example 1:**

But they run, yeah-heh yeah yeah  
Look what you're gonna lose that went to me, hey hey bop shoo-wop  
Better, 'cause I'm kissing you  
Burns my blue suede shoes  
All together now  
Quiet!  
Baby, shake it too much, darling  
It's driving me a yellow submarine

**Example 2:**

Any old enough to heaven  
No, 'round  
All you  
All together now  
All together, I sat on, don't sound  
Oh, honey, and boy been alone  
Love you  
Yeah

## License

This project is for educational and experimental purposes only.
