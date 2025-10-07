import pytest
import phone_utils as pu

@pytest.mark.parametrize('phone_number, expected',
    [('613-abc-hello', False),
     ('613-123-4567', True),
     ('1234567891', False)]
    )
def test_phone_utils(phone_number, expected):
    assert pu.is_valid_phone_number(phone_number) == expected

