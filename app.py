import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

#   open http://localhost:5000/albums
@app.route('/albums') # --> Defined a route (when I visit /albums URL, the below function will be executed)
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection) # --> Instance of AlbumRepository class, with database connection passed as argument
    albums = repo.all() # --> call all() method to retrieve all albums in the database
    return render_template("albums/index.html", albums=albums) 
    # Returns the rendered template and passes the albums variable to the template

@app.route('/albums/<id>')
def get_album_id(id):
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    album = repo.find(id)
    return render_template("albums/show.html", album=album)

@app.route('/artists/<id>')
def get_artist_id(id):
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist = repo.find(id)
    return render_template("albums/show_artists.html", artist=artist)

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artists = repo.all()
    return render_template("albums/artists_index.html", artists = artists)

@app.route('/albums/new', methods=['GET'])
def get_new_albums():
    return render_template("albums/new.html")

@app.route ('/albums', methods=['POST']) 
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    album = Album(None, title, release_year, 1)
    repository.create(album)
    return redirect(f"/albums/{album.id}")




# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
