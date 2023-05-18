from lib.album import *

"""
Album constructs with an id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test title", "Test release year", "Test id")
    assert album.id == 1
    assert album.title == "Test title"
    assert album.release_year == "Test release year"
    assert album.artist_id == "Test id"

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test title", "Test release year", "Test id")
    assert str(album) == "Album(1, Test title, Test release year, Test id)"

"""
We can compare two identical albums
And have them be equal.
"""
def test_albums_are_equal():
    album1 = Album(1, "Test title", "Test release year", "Test id")
    album2 = Album(1, "Test title", "Test release year", "Test id")
    assert album1 == album2