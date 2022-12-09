import random


class LyricsImporter:

    def __init__(self, num_prev_words=1):
        self.prev_words = []
        self.markov_chain_dict = {}
        self.num_prev_words = num_prev_words

    def __clear_prev_words(self):
        self.prev_words = ['\n' for _ in range(self.num_prev_words)]

    def __update_prev_words(self, word):
        self.prev_words.pop(0)
        self.prev_words.append(word)

    def __get_prev_words(self):
        return tuple(self.prev_words)

    def create_markov_chain_dict_from_folder(self, lyrics_folder):
        import os

        for root, dirs, files in os.walk(lyrics_folder, topdown=False):
            for name in files:
                path_file = os.path.join(root, name)
                file = open(path_file, "r")
                self.__clear_prev_words()
                for line in file:
                    self.create_markov_chain_dict(line)

    def create_markov_chain_dict(self, text):

        text = text.replace(',', ' ,').replace('?', ' ?').replace('\n', ' \n').replace('!', ' !')
        splits = text.split(" ")

        if text == ' \n':
            return

        # for loop to iterate over words array
        for curr_word in splits:
            curr_word = curr_word.replace('(', '').replace(')', '').replace('"', '')
            if curr_word in '':
                continue

            key = self.__get_prev_words()
            if key not in self.markov_chain_dict.keys():
                self.markov_chain_dict[key] = []

            self.markov_chain_dict[key].append(curr_word)

            self.__update_prev_words(curr_word)

    def create_lyrics(self, max_lines=8, max_words=100):
        lyrics = ''
        self.__clear_prev_words()
        num_lines = 1
        for _ in range(max_words):
            key = self.__get_prev_words()
            if key not in self.markov_chain_dict.keys():
                print('key not found: ', '-' + repr(key) + '-')
                break
            next_word = random.choice(self.markov_chain_dict[key])
            if next_word in [',', '!', '?', '\n'] and lyrics[-1] == ' ':
                lyrics = lyrics[:-1]
            lyrics += next_word

            if '\n' != next_word:
                lyrics += ' '
            else:
                num_lines += 1
            self.__update_prev_words(next_word)
            if num_lines > max_lines:
                break
        print(lyrics)


if __name__ == '__main__':

    lyrics_importer = LyricsImporter()
    lyrics_importer.create_markov_chain_dict_from_folder('./beatles_lyrics')
    lyrics_importer.create_lyrics()
