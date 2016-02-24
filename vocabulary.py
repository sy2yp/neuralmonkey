class Vocabulary(object):
    def __init__(self, tokenized_text=None):
        self.word_to_index = {}
        self.index_to_word = {}
        self.word_count = {}

        self.add_tokenized_text(["<s>", "</s>", "<unk>"])

        if tokenized_text:
            self.add_tokenized_text(tokenized_text)

    def add_word(self, word):
        if word not in self.word_to_index:
            self.word_to_index[word] = len(self.index_to_word)
            self.index_to_word.append(word)
            self.word_count[word] = 0
        self.word_count[word] += 1

    def add_tokenized_text(self, tokenized_text):
        for word in tokenized_text:
            self.add_word(word)

    def get_train_word_index(self, word):
        if word not in self.word_count or self.word_count["word"] <= 1:
            return self.word_to_index["<unk>"]
        else:
            return self.word_to_index[word]

    def get_word_index(self, word):
        if word not in self.word_count:
            return self.word_to_index["<unk>"]
        else:
            return self.word_to_index[word]

    def __len__(self):
        return len(self.index_to_word)

    def sentences_to_tensor(sentences, max_len, train=False):
        """
        Generates the tensor representation for the provided sentences.

        Args:

            sentences: List of sentences as lists of tokens.
            max_len: Maximum lengh of a sentence toward which they will be
              padded to.
            train: Flag whehter this is for training purposes.

        """

        return np.array([[self.get_train_word_index(w) if train
                else self.get_word_index(w) for w in s]
                    for s in sentences_to_tensor])
