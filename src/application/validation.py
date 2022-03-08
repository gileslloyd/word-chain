from __future__ import annotations
import os.path
import networkx as nx


class Validation:
    def validate_dictionary(self, dictionary_file: str) -> Validation:
        if not os.path.exists(dictionary_file):
            raise ValidationError(f"Dictionary file {dictionary_file} not found")

        if not open(dictionary_file, "r").readlines():
            raise ValidationError(f"Dictionary file {dictionary_file} is empty")

        return self

    def validate_words(
        self, word_graph: nx.Graph, start_word: str, end_word: str
    ) -> Validation:
        return self.validate_word(start_word, word_graph).validate_word(
            end_word, word_graph
        )

    def validate_word(self, word: str, word_graph: nx.Graph) -> Validation:
        if len(word) != 4:
            raise ValidationError("Start and end words must be 4 characters long")

        if not word_graph.has_node(word):
            raise ValidationError(f"{word} does not appear in dictionary")

        return self


class ValidationError(Exception):
    pass
