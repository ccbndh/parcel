from celery.result import AsyncResult
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks import task_get_data_from_spider


class TaskList(APIView):
    """
    List all snippets, or create a new task spider.
    """
    def get(self, request):
        task_id = request.query_params.get('task_id')
        if task_id:
            result = AsyncResult(task_id)
            if result.ready():
                return Response(result.result, status=status.HTTP_200_OK)
            return Response({'message': 'Result is not ready yet!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Missing param task_id'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        parcel_id = request.data.get('parcel_id')
        try:
            if parcel_id:
                task = task_get_data_from_spider.apply_async([parcel_id], expires=90, retry=True)
                return Response({'task_id': task.task_id}, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response({'message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': 'Parcel id must be not empty'}, status=status.HTTP_400_BAD_REQUEST)
