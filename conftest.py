import pytest
import networkx as nx


@pytest.fixture(scope='session')
def test_graph() -> nx.Graph:
    return nx.read_edgelist('./tests/unit/fixtures/word_graph.gz')