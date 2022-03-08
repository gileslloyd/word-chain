from typing import List
import pytest
import networkx as nx
from networkx.exception import NetworkXNoPath

from src.domain.wordchainservice import WordChainService


@pytest.mark.parametrize(
    "start_word,end_word,expected_chain",
    [
        ("spin", "spot", ["spin", "spit", "spot"]),
        ("hide", "sort", ["hide", "hire", "sire", "sore", "sort"]),
    ],
)
def test_the_shortest_chain_is_found(
    test_graph: nx.Graph, start_word: str, end_word: str, expected_chain: List[str]
) -> None:
    subject = WordChainService(test_graph)

    assert subject.find_chain(start_word, end_word) == expected_chain


def test_an_error_is_raised_if_a_chain_is_not_found(test_graph: nx.Graph) -> None:
    test_graph.add_node("axon")
    subject = WordChainService(test_graph)

    with pytest.raises(NetworkXNoPath):
        subject.find_chain("spin", "axon")
