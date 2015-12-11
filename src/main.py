import flask

import src

app = flask.Flask(__name__)
this_room = src.Room()


@app.errorhandler(404)
def entry_point(error):
    return flask.jsonify(dict(
        error="You're probably looking for /temperature/<time> ..."
    )), 400


@app.route("/temperature/<time>")
def temperature(time):
    temperature = this_room.get_temperature(time)
    if not temperature:
        response=dict(
            error="Sorry, we forgot the crystal ball at home, can't guess future temperature :("
        )
        code = 400
    else:
        response=dict(
            temperature=temperature
        )
        code = 200
    return flask.jsonify(response), code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
