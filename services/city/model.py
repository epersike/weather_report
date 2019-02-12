import requests
from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, Boolean, Table, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
 
Base = declarative_base()

'''
Sample:
{
	"uid": "d290f1ee-6c54-4b01-90e6-d701748f0851",
	"name": "Coca Coca LT 350ML",
	"brand": "Coca Cola",
	"manufacturer": {
		"name": "ACME Corporation",
		"homePage": "https://www.acme-corp.com",
		"phone": "47-9999-8888"
	},
	"barCode": "7891234567895"
}
'''

class City(Base):
	__tablename__ = 'city'
	
	id = Column(Integer, Sequence('city_id_seq'), primary_key=True)
	
	name = Column(String(250), nullable=False)

class Report(Base):
	__tablename__ = 'report'
	
	id = Column(Integer, Sequence('report_id_seq'), primary_key=True)

	date = Column(DateTime(), nullable=False)

	temp = Column(Float(precision=2))

	temp_min = Column(Float(precision=2))
	
	temp_max = Column(Float(precision=2)) 

	weather = Column(String(250))

	weather_icon = Column(String(4))

	wind_spd = Column(Float(precision=2))

	wind_dir = Column(Float(precision=2))

	city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
