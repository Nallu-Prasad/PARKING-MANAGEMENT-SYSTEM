import flask
from flask import render_template
import subprocess
import time

app = flask.Flask(__name__)

@app.route('/yield')
def index():
    def inner():
        for x in range(1000):
            yield '%s<br/>\n' % x
            time.sleep(1)
    return render_template('index.html', word=inner())
    #return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show the partial page immediately

app.run(debug=True, port=8080)