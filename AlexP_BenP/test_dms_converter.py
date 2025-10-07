import pytest
import dms_converter as dc

@pytest.mark.parametrize('dmsinput, expectedlong, expectedlat',
    [('075 45 03 W 45 23 05 N\n', -75.750833, 45.384722),
     ('075 45 03 w 45 23 05 n\n', -75.750833, 45.384722),
     ('075 45 03 w 91 23 05 n\n', None, None),
     ('-81 45 03 w 45 23 05 n\n', None, None),
     ('075 45 03 w 45 23 72 n\n', None, None),
     ('075 45 03 z 45 23 72 n\n', None, None)
     ]
    )
def test_dms_converter(dmsinput, expectedlong, expectedlat):
    assert dc.dms2dd(dmsinput) == (expectedlong, expectedlat)
    