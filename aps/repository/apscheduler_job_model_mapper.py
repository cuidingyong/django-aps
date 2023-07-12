"""
apscheduler job model mapper
"""
from django.db import DatabaseError

from aps.models import ApschedulerJobInfo


def add_apscheduler_job_info(job_info: dict):
    try:
        obj = ApschedulerJobInfo.objects.create(
            **job_info
        )
        return obj.id
    except DatabaseError:
        raise
