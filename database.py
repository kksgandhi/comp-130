def empty_db():
    return {}


def add_item(database, artist, artwork, year, description, owner):
    if artist in database:
        if artwork in database[artist]:
            return False
    else:
        database[artist] = empty_db()
    database[artist][artwork] = (year, description, owner)
    return True


def change_owner(database, artist, artwork, new_owner):
    if artist not in database:
        return False
    if artwork not in database[artist]:
        return False
    tempuple = database[artist][artwork]
    twempuple = (tempuple[0], tempuple[1], new_owner)
    database[artist][artwork] = twempuple
    return True

# Dictionary of artists, holds list of dictionary of artworks which map to tuple
# Artist name : {Artwork Name : (year, description, owner)}


def select_artist(database, artist):
    tempdb = {}
    if artist in database:
        tempdb[artist] = database[artist]
    return tempdb


def select_artwork(database, artwork):
    tempdb = {}
    for artist in database:
        if artwork in database[artist]:
            if artist not in tempdb:
                tempdb[artist] = {}
            tempdb[artist][artwork] = database[artist][artwork]
    return tempdb


def select_year(database, year):
    tempdb = {}
    for artist in database:
        for artwork in database[artist]:
            if year == database[artist][artwork][0]:
                if artist not in tempdb:
                    tempdb[artist] = {}
                tempdb[artist][artwork] = database[artist][artwork]
    return tempdb


def select_description(database, keyword):
    tempdb = {}
    for artist in database:
        for artwork in database[artist]:
            if keyword in database[artist][artwork][1]:
                if artist not in tempdb:
                    tempdb[artist] = {}
                tempdb[artist][artwork] = database[artist][artwork]
    return tempdb


def select_owner(database, owner):
    tempdb = {}
    for artist in database:
        for artwork in database[artist]:
            if owner == database[artist][artwork][2]:
                if artist not in tempdb:
                    tempdb[artist] = {}
                tempdb[artist][artwork] = database[artist][artwork]
    return tempdb


def sorted_database(database):
    artistkeys = sorted(list(database.keys()))
    return_list = []
    for key in artistkeys:
        artworkkeys = sorted(list(database[key].keys()))
        temp_artwork_list = []
        for art_piece_key in artworkkeys:
            temp_artwork_list.append(
                (art_piece_key, database[key][art_piece_key]))
        return_list.append((key, temp_artwork_list))
    return return_list


def format_results(database):
    database_sorted = sorted_database(database)
    return_string = ""
    for artist in database_sorted:
        return_string += artist[0]
        return_string += "\n    "
        for artwork in artist[1]:
            return_string += artwork[0]
            return_string += ", "
            for index in range(3):
                return_string += str(artwork[1][index])
                if index < 2:
                    return_string += ", "
            return_string += "\n    "
        return_string = return_string[:-4]
    return return_string


#
# Code for testing
#
# The code below will test your definitions.  Use this in addition to OwlTest.
