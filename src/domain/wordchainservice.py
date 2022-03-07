from __future__ import annotations
import string
from typing import List
import networkx as nx


class WordChainService:
    def __init__(self, word_graph: nx.Graph):
        self.word_graph = word_graph

    def find_chain(self, start_word: string, end_word: string) -> List[string]:
        return nx.shortest_path(self.word_graph, start_word, end_word)
