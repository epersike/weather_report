import requests
from datetime import datetime

import core

from .model import City as CityModel, Report as ReportModel

class Report:
    def __init__(self, dbsession=None):
        self.dbs = dbsession or core.dbsession

    def get_reports(self, city_name):
        req = self.request_from_ws(city_name)

        if not req:
            raise CityNotFoundException("City not found!")

        city, reports_list = self.parse(req)

        sess = self.dbs()

        C = sess.query(CityModel).filter_by(name=city['name']).first()
        if not C:
            
            C = CityModel(**city)
            sess.add(C)

        for rep in reports_list:
            R = sess.query(ReportModel).filter_by(date=rep['date'], city_id=C.id).first()

            if R:
                continue

            rep['city_id'] = C.id
            sess.add(ReportModel(**rep))

        sess.commit()

        return reports_list
	
    def request_from_ws(self, city_name):
        params = {
        'q': city_name,
        'mode': 'json',
        'appid': 'eb8b1a9405e659b2ffc78f0a520b1a46',
        'units': 'metric',
        }

        r = requests.get('http://api.openweathermap.org/data/2.5/forecast?', params=params)
        
        return r.json()

    def parse(self, req):
        city = {
            'id': req['city']['id'],
            'name': req['city']['name'],
        }

        report_list = []
        
        for rep in req['list']:
            report_list.append({
                'city_id': req['city']['id'],
                'date': datetime.strptime(rep['dt_txt'], '%Y-%m-%d %H:%M:%S'),
                'temp': rep['main']['temp'],
                'temp_min': rep['main']['temp_min'],
                'temp_max': rep['main']['temp_max'],
                'weather': rep['weather'][0]['main'],
                'weather_icon': rep['weather'][0]['icon'],
                'wind_spd': rep['wind']['speed'],
                'wind_dir': rep['wind']['deg'],
            })

        return (city, report_list)

class CityNotFoundException(Exception):
	pass


if __name__ == '__main__':
    Report(core.dbsession).get_reports('Timbó')