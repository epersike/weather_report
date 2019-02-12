import os, importlib, traceback
from connexion.resolver import RestyResolver
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import os, importlib
import sys

APPS_PATH = os.path.join('.\\', 'services')
APPS_LIST = []

dbname = 'weatherdb'

engine = create_engine('sqlite:///%s.db' % dbname)

for d in os.walk(APPS_PATH):
	if not 'model.py' in d[2]:
		continue

	basepath = d[0]

	APPS_LIST.append('.'.join(os.path.split(basepath[2:])))

def dbsession():
	return sessionmaker(bind=engine)()

def create_api(ws):
	'''
		Cria as apis buscando as mesmas dentro de todos os apps...
	'''

	for app in APPS_LIST:

		if app.endswith('help'):
			continue

		print('Criando apis de: %s ' % app)

		a = importlib.import_module(app)

		try:
			ws.add_api(os.path.join(list(a.__path__)[0], 'swagger.yaml'), options={"swagger_ui": False})
		except:
			print('endpoints para o service %s não foram encontrados' % a.__name__)
			print(traceback.format_exc())
			return

		print('APIs de %s importadas com sucesso' % str(a))

def checkdb(apps):

	producao = '--producao' in sys.argv

	print('Executando em modo producao: %s' % str(producao))

	for app in apps:
		app = '%s.model' % app

		print('Importando: %s ' % app)

		a = importlib.import_module(app)

		print('Importado com sucesso: %s' % a)

		# Cria um banco para cada app
		#dbname = app.split('.')[1]

		print('Criando o banco %s...' % dbname)

		# Create all tables in the engine. This is equivalent to "Create Table"
		# statements in raw SQL.
		if not hasattr(a, 'Base'):
			print('Atencao: package %s nao possui definicao de banco' % a.__name__)
			continue

		a.Base.metadata.create_all(engine)