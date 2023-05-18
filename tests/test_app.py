from playwright.sync_api import Page, expect

# Tests for your routes go here
"""
When we make a POST request to /albums
And we put no paramaters
Then we should get Expected response 400 Bad Request - "Invalid - You need to add an album"
"""
def test_invalid_post(web_client):
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Invalid - You need to add an album'


"""
When we make a POST request to /albums
And we put title, release_year, artist_id as the body parameters
Then we should get Expected response 200 OK - no content but details added
"""
def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post('/albums', data={'title': 'title1', 'release_year': '2023', 'artist_id': '1'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

"""
When we make a GET request to /albums
Then we should get Expected response 200 OK and we get the output of all records in our database
"""
def test_get_albums(web_client):
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Doolittle, 1989, 1), Album(2, Surfer Rosa, 1988, 1), Album(3, 'Waterloo', 1974, 2), Album(4, 'Super Trouper', 1980, 2), Album(5, 'Bossanova', 1990, 1), Album(6, 'Lover', 2019, 3), Album(7, 'Folklore', 2020, 3), Album(8, 'I Put a Spell on You', 1965, 4), Album(9, 'Baltimore', 1978, 4), Album(10, 'Here Comes the Sun', 1971, 4), Album(11, 'Fodder on My Wings', 1982, 4), Album(12, 'Ring Ring', 1973, 2)"
    

"""
When we make a GET request to /albums/1
Then we should get Expected response 200 OK and we get the output the first item
"""
def test_get_album_1(web_client):
    response = web_client.get('/albums/1')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Doolittle, 1989, 1)"

"""
When I make a GET request to /artists
Then I should get Expected response (200 OK) and the below output:
(Pixies, ABBA, Taylor Swift, Nina Simone)
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
When I make a POST request to /artists
With body parameters: name=Wild nothing, genre=Indie
Then I should get the Expected response (200 OK) and no content
(creates a new artist in the database)
"""
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

"""
When I make another GET request to /artists
Then I should get Expected response (200 OK) and the new list :
(Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing)
"""
def test_get_artists_with_new_name(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"


# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
