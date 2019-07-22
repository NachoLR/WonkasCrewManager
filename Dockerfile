FROM python:3

RUN mkdir /WonkasCrewManager

WORKDIR /WonkasCrewManager

COPY requirements.txt /WonkasCrewManager

RUN pip install -r requirements.txt

COPY . /WonkasCrewManager

CMD [ "python", "./WonkasCrewManager.py" ]
