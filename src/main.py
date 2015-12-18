import flask

from DistanceSensorImp import DistanceSensorImp
from InOutAdaptor import InOutAdaptor
from room import Room

app = flask.Flask(__name__)
this_room = Room()
adaptor = InOutAdaptor(1,200,1000,DistanceSensorImp(1),DistanceSensorImp(2))
adaptor.add_listener(this_room)


@app.errorhandler(404)
def entry_point(error):
    return flask.jsonify(dict(
        error="You're probably looking for /temperature/<time> ..."
    )), 400


@app.route("/people/")
def people():
    people = this_room.get_people()
    response = dict(people=people)
    code = 200
    return flask.jsonify(response), code

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
