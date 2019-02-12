import os, sys
import connexion

import core 

from flask import app, render_template

if __name__ == '__main__':

	if '--checkdb' in sys.argv:
		print('Executando manutenção no banco de dados...')
		core.checkdb(core.APPS_LIST)
		sys.exit(0)

	app = connexion.FlaskApp(__name__)

	@app.route('/')
	def main(name=None):
		print('main route')
		return render_template('index.html', name=name)

	core.create_api(app)

	app.run()

