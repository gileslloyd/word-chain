import string
from src.domain.networkfactory import NetworkFactory
from src.domain.wordchainservice import WordChainService


class App:
    def __init__(self, dictionary_file: string):
        network_factory = NetworkFactory()
        self._word_chain_service = WordChainService(network_factory.from_file(dictionary_file))

    def get_word_chain(self, start_word: string, end_word: string):
        print(self._word_chain_service.find_chain(start_word.lower(), end_word.lower()))
