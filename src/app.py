from typing import List
from pathlib import Path
import os

from src.application.validation import Validation
from src.domain.networkfactory import NetworkFactory
from src.domain.wordchainservice import WordChainService


class App:
    def __init__(self, dictionary_file: str):
        self._validation = Validation().validate_dictionary(dictionary_file)
        self._word_graph = NetworkFactory().from_file(dictionary_file)
        self._word_chain_service = WordChainService(self._word_graph)

    def run(self, start_word: str, end_word: str, result_file: str) -> None:
        filepath = f"./data/{result_file}"
        directory = os.path.dirname(filepath)

        if not os.path.exists(directory):
            Path(directory).mkdir(parents=True, exist_ok=True)

        with open(filepath, "w") as output:
            output.write("\n".join(self.get_word_chain(start_word, end_word)))

    def get_word_chain(self, start_word: str, end_word: str) -> List[str]:
        start_word = start_word.lower()
        end_word = end_word.lower()

        self._validation.validate_words(self._word_graph, start_word, end_word)

        return self._word_chain_service.find_chain(start_word, end_word)
