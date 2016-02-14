from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import check_watchdogs


class CheckwatchdogPermission(IsAuthenticated):

    def has_permission(self, request, view):
        return (
            super().has_permission(request, view) and
            request.user.has_perm('watchdog.check_watchdog')
        )


class CheckWatchdogsView(APIView):
    permission_classes = (CheckwatchdogPermission,)

    def post(self, request, *args, **kwargs):
        all_clear = check_watchdogs()
        return Response({'all_clear': all_clear}, status=status.HTTP_200_OK)
