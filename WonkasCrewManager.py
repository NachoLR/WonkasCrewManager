# coding=utf-8
# !flask/bin/python
from flask import Flask
from flask import request

from WonkasCrewApplication.WonkasOmmpaLoompaManagerCore import WonkasOmmpaLoompaManagerCore

WonkasOmmpaLoompaManagerCore = WonkasOmmpaLoompaManagerCore()

app = Flask(__name__)

"""
The server must fulfill the following API features:
⦁	Get the list of Oompa Loompas. For that list, only name, age and job are required per Oompa Looma.
⦁	Get the full detail of an Oompa Loompa
⦁	Add a new Oompa Loompa
⦁	Edit a current Oompa Loompa

"""

@app.route('/WonkaCrew', methods=['GET'])
def get_oompa_lompa_s():

    try:
        id_ol = request.args.get('id')

        if id_ol is None:
            response = WonkasOmmpaLoompaManagerCore.GetAllOompaLoompa()
        else:
            response = WonkasOmmpaLoompaManagerCore.GetOneOompaLoompa(id_ol)

    except Exception as e:
        response = "{Error: %s}" %(e,)
    return response

    return response



@app.route('/WonkaCrew', methods=['POST'])
def create_oompa_lompa():

    try:
        name_ol = request.args.get('name')
        age_ol = request.args.get('age')
        job_ol = request.args.get('job')
        height_ol = request.args.get('height')
        weight_ol = request.args.get('weight')
        description_ol = request.args.get('description')

        response = WonkasOmmpaLoompaManagerCore.InsertNewOompaLoompa(name_ol, age_ol, job_ol, height_ol, weight_ol, description_ol)

    except Exception as e:
        response = "{Error: %s}" %(e,)

    return response


@app.route('/WonkaCrew', methods=['PUT'])
def edit_oompa_lompa():

    try:
        id_ol = request.args.get('id')
        name_ol = request.args.get('name')
        age_ol = request.args.get('age')
        job_ol = request.args.get('job')
        height_ol = request.args.get('height')
        weight_ol = request.args.get('weight')
        description_ol = request.args.get('description')
        response = WonkasOmmpaLoompaManagerCore.UpdateOompaLoompa(id_ol, name_ol, age_ol, job_ol, height_ol, weight_ol, description_ol)
    except Exception as e:
        response = "{Error: %s}" % (e,)


    return response


if __name__ == '__main__':
    app.run(debug=True)