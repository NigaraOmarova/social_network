from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from todo_app.serializers import TaskSerializer

from todo_app.models import Task


@api_view(['GET'])
def api_overview_links(request):
    urls = {
        'lists_todo':'task-list',
        'detail_todo': '/task-detail/<int:pk>',
        'create_todo': '/task-create/',
        'edit_todo': '/task-edit/<int:pk>/',
        'delete_todo': '/task-delete/<int:pk>/'
    }
    for key in urls:
        urls[key] = request.build_absolute_uri() + urls[key]
    return Response(urls)


@api_view(['GET'])
def get_task_list(request):
    tasks = Task.objects.all()
    print(tasks)
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task,many=False)
    except Task.DoesNotExist as error:
        print(error)
        raise Http404
    return Response(serializer.data)


@api_view(['PUT'])
def task_edit(request,pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task,data=request.data)
        if serializer.is_valid():
            print('isvalid')
            serializer.save()
    except Task.DoesNotExist as error:
        print(error)
        raise Http404
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response("Task deleted successfully", status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist as error:
        raise Http404
