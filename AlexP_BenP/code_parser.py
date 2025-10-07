def get_db_link(building_code):
    dblink = ''
    dblink += ''.join(building_code[i] for i in range(4,6))
    dblink += '-'
    dblink += ''.join(building_code[i] for i in range(10,13))
    print(dblink)
    return dblink