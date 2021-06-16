from logging import debug
from flask import Flask
from flask.templating import render_template
from redis import Redis
from flask_caching import Cache

from flask_debugtoolbar import DebugToolbarExtension


# the toolbar is only enabled in debug mode:

# set a 'SECRET_KEY' to enable the Flask session cookies

redis=Redis()
cache = Cache(config={
    "CACHE_TYPE": 'redis'
})

app=Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = 'asdasdasdas'
cache.init_app(app)
toolbar = DebugToolbarExtension(app)


@app.route('/')
@cache.cached(timeout=1200)
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run()