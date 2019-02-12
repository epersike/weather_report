# Weather Report Sample Web App

This is a simple Web App to view weather reports on searched cities

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. This project was not meant to be deployable (yet).

### Prerequisites

Everything you need is in requirements.txt, just run it like:

```
pip install -r requirements.txt
```

connexion (and dependencies)
sqlalchemy (and dependencies)

## Running the server

1. Install python 3.7 or superior;
2. Run ```pip install -r requirements.txt```;
3. Run ```python main.py --checkdb``` (To initialize the database);
4. Run ```python main.py``` to start the webserver;
5. Access ```http://127.0.0.1:5000``` on your web browser;
6. Track your city's weather by searching it's name;

## Testing 

The postman folder inside the package contains Postman's requests and envinroment variables that can be used both to test the application's APIs and the OpenWeather API. Make sure you have imported both and selected the correct envinronment so you can use it. For the ```weather_report``` folder requests, make sure you have the ```main.py``` webserver running.

Unit tests not quite implemented yet, but will be like:

```
python tests.py
```

Every service implemented will have it's own unit tests.

## Authors

* **Einar** - *Initial work* - [EinarXQ](https://github.com/einarXQ)

## License

This is just a sample app, you may use it at your own will and risk.
