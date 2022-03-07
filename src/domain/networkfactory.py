from typing import List

import networkx as nx
import pandas as pd


class NetworkFactory:
    def from_file(self, file_path: str) -> nx.Graph:
        return self.from_series(self._read_file(file_path))

    def from_series(self, words: pd.Series) -> nx.Graph:
        word_graph = nx.Graph()

        for word in words:
            for i in range(0, 4):
                adjacent_words = words[words.str.contains(r'{}.{}'.format(word[0:i], word[i + 1:])) & (words != word)]
                word_graph.add_edges_from(list(zip([word] * len(adjacent_words), adjacent_words)))

        return word_graph

    def _read_file(self, file_path: str) -> pd.Series:
        words = pd.read_csv(file_path, header=None)

        words = words[words[0].str.len() == 4]

        return words[words[0].str.contains(r'^[A-Za-z]+')][0].str.lower()
