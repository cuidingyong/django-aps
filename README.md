# Django APScheduler Register

Django-aps adds the task registration discovery function on the basis of A,
which is more convenient for users to realize the configuration of scheduled tasks.

## Installation

```commandline
pip install django-aps
```

## Quick start

- Add ``aps`` to your ``INSTALLED_APPS`` setting like this:

```python
INSTALLED_APPS = (
    # ...
    "django_apscheduler",
    "django_aps",
)
```

- django-aps comes with sensible configuration defaults out of the box. The defaults can be overridden by adding
  the following settings to your Django `settings.py` file:

```python
# Default apscheduler functions which discovered is saved in database, you can change the settings
# to change it.
APS_SETTINGS = {
    'DEFAULT_DISCOVER_SCHEMA': 'pkg',
}
```

- Run `python manage.py migrate` to create the django_apscheduler models.

- Register a APScheduler function in your project(use decorator `aps_register`):

```python
from django_aps.utils.register import aps_register


@aps_register
def add(num1, num2):
    print(num1 + num2)


class Demo:

    @aps_register
    def subtract(self, sub1, sub2):
        print(sub1 - sub2)
```

- Auto discover APScheduler function:

```shell
curl --location 'http://127.0.0.1:8000/aps/func/query'
# You can also filter by func_name like this:
curl --location 'http://127.0.0.1:8000/aps/func/query?func_name=add'
# Return:
{
    "success": true,
    "code": 1,
    "data": [
        {
            "func_module": "apps.foundation.service.aps_test",
            "func_name": "add",
            "func_args": [
                "num1",
                "num2"
            ],
            "func_doc": null
        },
        {
            "func_module": "apps.foundation.service.aps_test",
            "func_name": "Demo.subtract",
            "func_args": [
                "self",
                "sub1",
                "sub2"
            ],
            "func_doc": null
        }
    ]
}
```

- Add APScheduler:

```shell
curl --location 'http://127.0.0.1:8000/aps/scheduler-job/add' \
--header 'Content-Type: application/json' \
--data '{
    "name": "demo",
    "func_module": "apps.foundation.service.aps_test",
    "func_name": "add",
    "func_args": [],
    "func_kwargs": {
        "num1": 100,
        "num2": 2
    },
    "trigger": {
        "trigger_type": "cron",
        "trigger_params": {
            "year": "*",
            "day_of_week": "0-4",
            "hour": "16",
            "minute": "50",
            "second": "0"
        }
    }
}'
```

## Submitting bugs

You can report issues directly on Github, that would be a really useful contribution given that we lack some user
testing on the project. Please document as much as possible the steps to reproduce your problem (even better with
screenshots).

## Updates
