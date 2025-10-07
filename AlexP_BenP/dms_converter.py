def dms2dd (dmsinput):

    dmsinput = dmsinput.strip().upper()

    if len(dmsinput) != 22:
        return None, None

    dmsparts = dmsinput.split()
    long_deg = int(dmsparts[0])
    long_min = int(dmsparts[1])
    long_sec = int(dmsparts[2])
    long_dir = dmsparts[3]
    lat_deg = int(dmsparts[4])
    lat_min = int(dmsparts[5])
    lat_sec = int(dmsparts[6])
    lat_dir = dmsparts[7]

    if long_deg < 0 or long_deg > 180 or long_min < 0 or long_min > 60 or long_sec < 0 or long_sec > 60:
        return None, None
    if lat_deg < 0 or lat_deg > 90 or lat_min < 0 or lat_min > 60 or lat_sec < 0 or lat_sec > 60:
        return None, None
    if long_dir != 'W' and long_dir != 'E':
        return None, None
    if lat_dir != 'N' and lat_dir != 'S':
        return None, None
     
    longdd = (long_deg + long_min/60 + long_sec/3600)
    latdd = (lat_deg + lat_min/60 + lat_sec/3600)

    if long_dir == "W":
        longdd = -longdd
    if lat_dir == "S":
        latdd = -latdd

    return round(longdd,6), round(latdd,6)