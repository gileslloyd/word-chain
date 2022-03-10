import networkx as nx
import pandas as pd
from pandarallel import pandarallel


pandarallel.initialize()


class NetworkFactory:
    def from_file(self, file_path: str) -> nx.Graph:
        return self.from_series(self._read_file(file_path))

    def from_series(self, words: pd.Series) -> nx.Graph:
        word_graph = nx.Graph()

        for i, row in self._get_edge_list(words).iterrows():
            word_graph.add_edges_from(list(zip([row[0]] * len(row['adj']), row['adj'])))

        return word_graph

    def _read_file(self, file_path: str) -> pd.Series:
        words = pd.read_csv(file_path, header=None)

        words = words[words[0].str.len() == 4]

        return words[words[0].str.contains(r"^[A-Za-z]+")][0].str.lower()

    def _get_edge_list(self, words: pd.Series) -> pd.DataFrame:
        edge_list = pd.DataFrame(words)

        def find_adjacent_words(word, words):
            return list(words[words.str.contains(
                r'({0}[^{1}]+{2}{3}|[^{0}]+{1}{2}{3}|{0}{1}[^{2}]+{3}|{0}{1}{2}[^{3}]+?)'.format(*list(word))
            )])

        edge_list['adj'] = words.parallel_apply(find_adjacent_words, words=words)

        edge_list.set_index(0)

        return edge_list
