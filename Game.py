import requests
from datetime import datetime, timedelta


class Ets2:
    def __init__(self, url):
        #url = 'http://192.168.1.172:25555/api/ets2/telemetry'
        self.url = url
        self.request = requests.get(self.url, allow_redirects=True)
        self.game = Game(request=self.request)
        self.trailer = trailer(request=self.request)
        self.job = job(request=self.request)
        self.navigation = navigation(request=self.request)

    def expected_real_time(self):
        return self.navigation.estimatedTime / self.game.timeScale[0]

    def expected_real_arriv(self):
        return datetime.now() + self.expected_real_time()


class Game:
    def __init__(self, request: requests):
        self.json = request.json()['game'],
        self.connected = (request.json()['game']['connected']),
        self.gameName = request.json()['game']['gameName'],
        self.paused = request.json()['game']['paused'],

        # -- Time in Game
        self.time_t = request.json()['game']['time'],
        self.time = datetime.strptime(self.time_t[0].replace(str(str(self.time_t[0])[0:4]), "2016"),
                                      '%Y-%m-%dT%H:%M:%SZ'),
        scale = request.json()['game']
        self.timeScale = scale['timeScale'],
        # -- Next Rest Stop Time
        self.nextRestStopTime1 = request.json()['game']['nextRestStopTime'],
        self.nextRestStopTime = datetime.strptime(
            self.nextRestStopTime1[0].replace(str(str(self.nextRestStopTime1[0])[0:4]), "2016"),
            '%Y-%m-%dT%H:%M:%SZ'),

        self.version = request.json()['game']['version'],
        self.telemetryPluginVersion = request.json()['game']['telemetryPluginVersion']


class trailer:
    def __init__(self, request: requests):
        self.json = request.json()['trailer'],
        self.attached = request.json()['trailer']['attached'],
        self.id = request.json()['trailer']['id'],
        self.name = request.json()['trailer']['name'],
        self.mass = request.json()['trailer']['mass'],
        self.wear = request.json()['trailer']['wear'],
        self.placement = None


class job:
    def __init__(self, request: requests):
        self.json = request.json()['job'],
        self.income = request.json()['job']['income'],

        deadlineTime1 = request.json()['job']['deadlineTime']
        # self.deadlineTime = datetime.strptime(str(deadlineTime1[0]).
        #                                      replace((deadlineTime1[0])[0:4],
        #                                              "2016"), '%Y-%m-%dT%H:%M:%SZ'),

        remainingTime = request.json()['job']['remainingTime']
        h, m, s = str(remainingTime)[-9:][:8].split(":")
        self.remainingTime = timedelta(hours=int(h), minutes=int(m), seconds=int(s)),

        self.sourceCity = request.json()['job']['sourceCity'],
        self.sourceCompany = request.json()['job']['sourceCompany'],
        self.destinationCity = request.json()['job']['destinationCity'],
        self.destinationCompany = request.json()['job']['destinationCompany'],


class navigation:
    def __init__(self, request: requests):
        self.json = request.json()['navigation'],

        estimatedTime = request.json()['navigation']['estimatedTime']
        h, m, s = str(estimatedTime)[-9:][:8].split(":")
        self.estimatedTime = timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        self.estimatedDistance = request.json()['navigation']['estimatedDistance'],
        self.speedLimit = request.json()['navigation']['speedLimit']


