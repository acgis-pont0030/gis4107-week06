import pytest
import doc_scanner as ds

@pytest.mark.parametrize('in_text, expected',
    [('abcdefg', False),
     ('abcTx6op3defg', True)]
    )
def test_has_x_code(in_text, expected):
    assert ds.has_x_code(in_text) == expected

@pytest.mark.parametrize('in_text, expected',
    [('abcdefg', -1),
     ('abcTx6op3defg', 4)]
    )
def test_get_x_code_position(in_text, expected):
    assert ds.get_x_code_position(in_text) == expected