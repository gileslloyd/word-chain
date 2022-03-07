import string
from src.application.validation import Validation
from src.domain.networkfactory import NetworkFactory
from src.domain.wordchainservice import WordChainService


class App:
    def __init__(self, dictionary_file: string):
        self._validation = Validation().validate_dictionary(dictionary_file)
        self._word_graph = NetworkFactory().from_file(dictionary_file)
        self._word_chain_service = WordChainService(self._word_graph)

    def get_word_chain(self, start_word: string, end_word: string):
        start_word = start_word.lower()
        end_word = end_word.lower()

        self._validation.validate_words(self._word_graph, start_word, end_word)

        print(self._word_chain_service.find_chain(start_word, end_word))
