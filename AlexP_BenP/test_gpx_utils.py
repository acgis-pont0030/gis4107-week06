import pytest
import gpx_utils as gpx_u

@pytest.mark.parametrize('gpx, expected',
    [('<trkpt lat="45.3888995" lon="75.7472631">', (45.3888995, 75.7472631)),
     ('<trkpt lat="-45.3888995" lon="75.7472631">', (-45.3888995, 75.7472631)),
     ('<trkpt lat="45.3888995" lon="-75.7472631">', (45.3888995, -75.7472631)),
     ('<trkpt lat="-45.3888995" lon="-75.7472631">', (-45.3888995, -75.7472631))
    ])
def test_get_coords_from_gpx(gpx, expected):
    assert gpx_u.get_coords_from_gpx(gpx) == expected