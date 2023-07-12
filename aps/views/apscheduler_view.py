"""
Apscheduler functions view
"""
from django.http import JsonResponse

from aps.base import BaseGenericAPIView
from aps.serializers.apscheduler_serializers import RegisteredFuncQuerySerializers, SchedulerJobAddSerializers
from aps.service.discover_service import DiscoverService


class RegisteredFuncQueryView(BaseGenericAPIView):
    serializer_class = RegisteredFuncQuerySerializers

    def get(self, request):
        serializer = self.serializer_class(data=request.query_params)
        self.check_validate(serializer)
        data = serializer.validated_data
        aps_funcs = DiscoverService().get_apscheduler_funcs(data.get('name'))

        return JsonResponse(
            data={
                'success': True,
                'code': 1,
                'data': aps_funcs
            }
        )


class SchedulerJobAddView(BaseGenericAPIView):
    serializer_class = SchedulerJobAddSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        self.check_validate(serializer)
        data = serializer.validated_data
