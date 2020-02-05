from flask import Flask, render_template, request, url_for
import generate.generate as gg
import re
from clear import strToDict





app = Flask(__name__, static_url_path="/static")


@app.route('/')
def init():
    forward_message = gg.generate1.g_data
    return render_template("main.html", forward_message=forward_message)


@app.route("/gen", methods=["POST"])
def program():
    data = str(request.data)[2:len(str(request.data)) - 1]
    l = re.findall("\{\"program\":\"[0-9]*\",\"velocity\":[a-z]*,\"length\":[a-z]*,\"offset\":[a-z]*\}", data)
    settingsList = list()
    for i in l:
        preSetting = strToDict(i)
        settingsList.append(gg.Instrument_Settings(program=preSetting["program"], velocity=preSetting["velocity"],length=preSetting["length"],offset=preSetting["offset"]))

    midi_song = gg.generate1.generate(settingsList)
    return url_for('static', filename=midi_song[10:])




if __name__ == '__main__':
    app.run(threaded=False)






