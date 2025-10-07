import pytest
import code_parser as cp

@pytest.mark.parametrize('building_code, expected',
    [('20-WBO-109642-809', 'BO-642')]
    )
def test_code_parser(building_code, expected):
    assert cp.get_db_link(building_code) == expected