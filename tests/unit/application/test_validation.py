import pytest
import networkx as nx
from src.application.validation import ValidationError, Validation


invalid_words = ['frog', 'too', 'supercalifragilisticexpialidocious', '$%^', '42', 'jocy', 'thit', 'them']

valid_words = ['spin', 'spit', 'spot', 'hide', 'side', 'sire', 'sore', 'sort']


@pytest.fixture(scope='module')
def validation() -> Validation:
    return Validation()


@pytest.fixture
def empty_dictionary(tmp_path) -> str:
    d = tmp_path / 'empty_dictionary.txt'
    d.write_text('')

    return str(d.resolve())


@pytest.fixture
def test_dictionary(tmp_path) -> str:
    d = tmp_path / 'test_dictionary.txt'
    d.write_text('\n'.join(valid_words))

    return str(d.resolve())


def test_an_error_is_raised_if_dictionary_doesnt_exist(validation) -> None:
    with pytest.raises(ValidationError):
        validation.validate_dictionary('not/a/file.path')


def test_an_error_is_raised_if_dictionary_is_empty(validation, empty_dictionary) -> None:
    with pytest.raises(ValidationError):
        validation.validate_dictionary(empty_dictionary)


def test_an_error_is_not_raised_if_dictionary_is_valid(validation, test_dictionary) -> None:
    try:
        validation.validate_dictionary(test_dictionary)
    except ValidationError:
        assert False, 'A validation exception was raised'


@pytest.mark.parametrize('start_word', invalid_words)
def test_an_error_is_raised_for_invalid_start_words(
        validation: Validation,
        start_word: str,
        test_graph: nx.Graph
) -> None:
    with pytest.raises(ValidationError):
        validation.validate_words(test_graph, start_word, 'sort')


@pytest.mark.parametrize('end_word', invalid_words)
def test_an_error_is_raised_for_invalid_end_words(
        validation: Validation,
        end_word: str,
        test_graph: nx.Graph
) -> None:
    with pytest.raises(ValidationError):
        validation.validate_words(test_graph, 'spin', end_word)


@pytest.mark.parametrize('invalid_word', invalid_words)
def test_we_can_validate_both_words_at_once(validation: Validation, invalid_word: str, test_graph: nx.Graph) -> None:
    with pytest.raises(ValidationError):
        validation.validate_words(test_graph, 'spin', invalid_word)

    with pytest.raises(ValidationError):
        validation.validate_words(test_graph, invalid_word, 'spin')


@pytest.mark.parametrize('valid_word', valid_words)
def test_no_errors_are_raised_for_valid_words(validation: Validation, valid_word: str, test_graph: nx.Graph) -> None:
    try:
        validation.validate_words(test_graph, valid_word, valid_word)
    except ValidationError:
        assert False, 'A validation exception was raised'
