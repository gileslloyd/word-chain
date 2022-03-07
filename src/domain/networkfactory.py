import networkx as nx
import pandas as pd


class NetworkFactory:
    def from_file(self, file_path: str) -> nx.Graph:
        words = pd.read_csv(file_path, header=None)

        words = words[words[0].str.len() == 4]
        words = words[words[0].str.contains(r'^[A-Za-z]+')][0].str.lower()

        word_graph = nx.Graph()

        for word in words:
            for i in range(0, 4):
                adjacent_words = words[words.str.contains(r'{}.{}'.format(word[0:i], word[i + 1:])) & (words != word)]
                word_graph.add_edges_from(list(zip([word] * len(adjacent_words), adjacent_words)))

        return word_graph
