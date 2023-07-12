"""
APScheduler Service
"""
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django.utils.module_loading import import_string

from aps.repository import apscheduler_job_model_mapper
from aps.settings import aps_settings

logger = logging.getLogger(__name__)


class APSchedulerService:

    def __init__(self):
        self._scheduler_options = None
        # self._scheduler = None
        self._start()

    def _start(self):
        scheduler_options = self._init_scheduler_options()
        self._scheduler = BackgroundScheduler(**scheduler_options)
        try:
            self._scheduler.start()
            logger.info('APScheduler has started')
        except Exception as e:
            logger.error(e, exc_info=True)
            self._scheduler.shutdown()

    def _init_scheduler_options(self):
        job_stores_cls = import_string(aps_settings.DEFAULT_JOB_STORES)
        jobstores = {
            'default': job_stores_cls()
        }
        default_executors = aps_settings.DEFAULT_EXECUTORS
        executors_cls = import_string(default_executors.get('executor'))
        executor = {
            'default': executors_cls(default_executors.get('max_pool_size'))
        }
        job_defaults = aps_settings.DEFAULT_JOB_DEFAULTS
        timezone = aps_settings.DEFAULT_TIMEZONE
        self._scheduler_options = {
            'jobstores': jobstores,
            'executor': executor,
            'job_defaults': job_defaults,
            'timezone': timezone
        }

        return self._scheduler_options

    def add_scheduler_job(self, name: str, func_module: str, func_name: str, func_args: list = None,
                          func_kwargs: dict = None, trigger: dict = None, description: str = None):
        """
        新增定时任务

        """
        func_ref = func_module + ':' + func_name
        trigger_params = trigger.get('trigger_params')
        trigger_type = trigger.get('trigger_type')
        job_info = {
            'name': name,
            'func_ref': func_ref,
            'func_name': func_name,
            'func_args': func_args,
            'func_kwargs': func_kwargs,
            'trigger_type': trigger_type,
            'trigger_params': trigger_params,
            'description': description
        }
        job_info_id = apscheduler_job_model_mapper.add_apscheduler_job_info(job_info)
        # self._scheduler.add_job(func=func_ref, trigger=)
