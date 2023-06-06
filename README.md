[![dneupan1](https://circleci.com/gh/dneupan1/django_test.svg?style=svg)](https://app.circleci.com/pipelines/github/dneupan1/django_test)
## Development Guide
### Code changes, dependency management
Project uses pipenv for dependency management. Pycharm configuration files are added in the repository to make it easier
to setup development environment.
CircleCI configuration file has been added to make sure no commits break the repository. Please be mindful of the
build status once your changes have been pushed into the repository.
Before committing any changes, if there has been dependency changes, as in new dependencies are added, please regenerate
the requirements.txt file. CircleCI build takes requirements.txt for dependency resolution during build.
> pipenv requirements > requirements.txt

### Creating a new SQLite database
To create a new SQLite database, run the following command
python manage.py migrate

### Running the development server
To run the development server on local machine run the following command:
> python manage.py runserver  127.0.0.1:8000

You should be able to view the webpage at 127.0.0.1:8000

### Running the unit tests
Project uses pytest to Use the following command to run the unit test:
>pytest

 

## Deployment Guide
To run the ASGI application, use the following command:
>python -m uvicorn myproject.asgi:application

To deploy on a linux machine, use the following command:
>python -m gunicorn myproject.asgi:application -k uvicorn.workers.UvicornWorker

TODO: Figure out a way to deploy in windows


#### Note: All references have been taken from Djago's official documentation.
https://docs.djangoproject.com/en/4.2/howto/deployment/


