from rest_framework.decorators import api_view
from rest_framework.response import Response

from planning_app.serializers import TaskSerializer

from todo_app.models import Task


@api_view(['GET'])
def get_task_list(request):
    tasks = Task.objects.all()
    print(tasks)
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)
