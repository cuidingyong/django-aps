import os

from django.apps import AppConfig


class ApsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "aps"

    def ready(self):
        run_once = os.environ.get('CMDLINE_RUNNER_RUN_ONCE')
        if run_once is not None:
            return
        os.environ['CMDLINE_RUNNER_RUN_ONCE'] = 'True'

        _sync_aps()


def _sync_aps():
    from aps.utils.common import check_table_exist
    if check_table_exist('django_apscheduler_func'):
        from aps.service.discover_service import DiscoverService
        DiscoverService.sync_aps_to_db()
