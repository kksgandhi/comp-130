"""This code manages a database full of artists, artworks, and relevant information about the artwork. This file also contains many methods that manage those databases"""


def empty_db():
    """Returns an empty database"""
    return {}


def add_item(database, artist, artwork, year, description, owner):
    """Dr. Greiner said that the descriptions on canvas could be copied as docstrings, so here goes:Mutates the database to add one artwork. The database need not contain anything by that artist previously. However, if this is a duplicate artwork name for a particular artist, it instead does not mutate the database. It does not print any error message in this case. It returns a Boolean True or False indicating whether the artwork was added to the database"""
    if artist in database:
        if artwork in database[artist]:
            return False
    else:
        database[artist] = empty_db()
    database[artist][artwork] = (year, description, owner)
    return True


def change_owner(database, artist, artwork, new_owner):
    """Mutates the database to change the owner of the indicated artwork by the indicated artist. If no such artwork is in the database, there is no mutation. It returns a Boolean indicating whether the artwork ownership was updated"""
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
    """Returns a new database with all of the information for the given artist in the given database"""
    tempdb = {}
    if artist in database:
        tempdb[artist] = database[artist]
    return tempdb


def select_artwork(database, artwork):
    """ Returns a new database with all of the information for any artwork with the given name in the given database."""
    tempdb = {}
    for artist in database:
        if artwork in database[artist]:
            if artist not in tempdb:
                tempdb[artist] = {}
            tempdb[artist][artwork] = database[artist][artwork]
    return tempdb


def select_year(database, year):
    """
  Returns a new database with all of the information for any artwork from the given year in the given database   """
    tempdb = {}
    for artist in database:
        for artwork in database[artist]:
            if year == database[artist][artwork][0]:
                if artist not in tempdb:
                    tempdb[artist] = {}
                tempdb[artist][artwork] = database[artist][artwork]
    return tempdb


def select_description(database, keyword):
    """
 Returns a new database with all of the information for any artwork having a description containing the given keyword in the given database.   """
    tempdb = {}
    for artist in database:
        for artwork in database[artist]:
            if keyword in database[artist][artwork][1]:
                if artist not in tempdb:
                    tempdb[artist] = {}
                tempdb[artist][artwork] = database[artist][artwork]
    return tempdb


def select_owner(database, owner):
    """
 Returns a new database with all of the information for any artwork owned by the given owner in the given database   """
    tempdb = {}
    for artist in database:
        for artwork in database[artist]:
            if owner == database[artist][artwork][2]:
                if artist not in tempdb:
                    tempdb[artist] = {}
                tempdb[artist][artwork] = database[artist][artwork]
    return tempdb


def sorted_database(database):
    """
 Returns all the database contents, but in sorted order.  Artists are in alphabetical order by name, and within each artist, the artworks are in alphabetical order by name.   """
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
    """
 Returns a single string with all the information in the database, in sorted order.  The artist name is put on a line by itself.  All artworks by that artist are put on the following lines, one line per artwork.  Each line starts with four spaces, then lists artwork, year, description, and owner, each separated by a comma and a single space.  Each line ends in a newline character and has no spaces at the end.   """
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
