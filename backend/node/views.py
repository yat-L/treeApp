from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NodeSerializer
from .models import Node
import csv
import json

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'view-all':'/nodes/',
        'get-tree':'/get-tree',
        'update_node': '/nodes-update/<str:pk>',
        'create_node': '/nodes-create/',
        'delete_node': '/nodes-delete/<str:pk>',
        'export_csv': '/nodes-export/'
    }
    return Response(api_urls)

@api_view(['GET'])
def viewAll(request):
    nodes = Node.objects.all().order_by('nid')
    serializer = NodeSerializer(nodes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createNode(request ):
	serializer = NodeSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def updateNode(request, pk):
	node = Node.objects.get(nid=pk)
	serializer = NodeSerializer(instance=node, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def deleteNode(request, pk):
	node = Node.objects.filter(nid=pk)
	node.delete()

	return Response('Item deleted.')


@api_view(['GET'])
def getTree(request ):
    filename = "tree_data.csv"

    with open(filename, 'r') as csvFile:
        csvReader = csv.DictReader(csvFile,delimiter='\t')
        for row in csvReader:
            row['nid'] = row.pop('id')
            node = Node(**row)
            node.save()

    nodes = Node.objects.all().order_by('nid')
    serializer = NodeSerializer(nodes, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def exportCSV(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Exporting-Tree': 'attachment; filename="export.csv"'},
    )
    nodes = Node.objects.all().order_by('nid')
    fieldname = ['nid','name','description','parent','read_only']
    writer = csv.DictWriter(response, fieldnames=fieldname,delimiter='\t')
    writer.writeheader()
    for n in nodes:
        dictForm = model_to_dict(n)
        dictForm.pop('id')
        print(dictForm)
        writer.writerow(dictForm)

    return response

