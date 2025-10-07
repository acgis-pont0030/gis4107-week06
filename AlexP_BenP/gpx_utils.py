def get_coords_from_gpx(gpx):
    if gpx[1:6] == 'trkpt' and len(gpx) == 41 or len(gpx) == 42 or len(gpx) == 43:
        lat_index = gpx.index('lat')    #7
        lon_index = gpx.index('lon')    #24

        if gpx[lat_index+5] == '-':
            lat_num_range = (lat_index+5,lat_index+16)
        else:
            lat_num_range = (lat_index+5,lat_index+15)
        if gpx[lon_index+5] == '-':
            lon_num_range = (lon_index+5,lon_index+16)
        else:
            lon_num_range = (lon_index+5,lon_index+15)

        latitude = float(gpx[lat_num_range[0]:lat_num_range[1]])
        longitude = float(gpx[lon_num_range[0]:lon_num_range[1]])
        return (latitude, longitude)
    else:
        return (None, None)

print('<trkpt lat="45.3888995" lon="-75.7472631">')
print(get_coords_from_gpx('<trkpt lat="45.3888995" lon="-75.7472631">'))
print(type(get_coords_from_gpx('<trkpt lat="45.3888995" lon="-75.7472631">')))



# '<trkpt lat="45.3888995" lon="-75.7472631">'
# '012345678901234567890123456789012345678901'
# '0         1         2         3         4 '