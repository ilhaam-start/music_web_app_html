from playwright.sync_api import Page, expect

# Tests for your routes go here
def test_get_album_details(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Doolittle",
        "Surfer Rosa"
    ])

def test_visit_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    h1_tag = page.locator(".t-title")
    expect(h1_tag).to_have_text("Title: Surfer Rosa")
    paragraph_tag = page.locator(".t-release_year")
    expect(paragraph_tag).to_have_text("Released: 1988")

def test_get_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/artists/2")
    name_element = page.locator(".t-name")
    expect(name_element).to_have_text("Artist: ABBA")
    genre_element = page.locator(".t-genre")
    expect(genre_element).to_have_text("Genre: Pop")

def test_get_all_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/artists")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ])

def test_create_new_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add a new album'")
    page.fill("input[name=title]", "My Album")
    page.fill("input[name=release_year]", "2023")
    page.click("text='Add an album'")
    h1_tag = page.locator(".t-title")
    expect(h1_tag).to_have_text("Title: My Album")
    paragraph_tag = page.locator(".t-release_year")
    expect(paragraph_tag).to_have_text("Released: 2023")


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
