# Deployment Experiments

A series of deployments to try and iron out issues when deploying to Heroku.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

1. Create a fresh folder then move inside and issue command:

```
virtualenv .
```
2. Activate virtualenv 

Windows:

```
Scripts\activate.bat
```

Mac:

```
source bin/activate
```

### Installing

1. Install dependenices by issuing command:

```
pip install -r requirements.txt
```

2. Locate manage.py file and run the dev server from that location

```
python manage.py runserver
```

3. Go to http://127.0.0.1:8000/ where application should be running


## Running the tests

Run tests (functional and unit) with following command:

```
python manage.py test
```

## Deployment

TBC

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Selenium](https://selenium-python.readthedocs.io/) - Functional/User Journey automated tests

## Contributing

TBC

## Versioning

TBC

## Authors

* **Gav McClary

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
