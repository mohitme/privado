from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from data.models import Template
from data.serializers import TemplateSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET', 'POST'])
def tdata(request, customer_id):
    if request.method == 'GET':
        try:
            t = Template.objects.filter(customerId=customer_id)
            #t = Template.objects.all()
            template_serializer = TemplateSerializer(t, many=True)
            if template_serializer.data == []:
                return JsonResponse({'Message': 'The template with this customerId doesn''t exist'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return JsonResponse(template_serializer.data, safe=False)
        except Template.DoesNotExist:
            return JsonResponse({'Message': 'The template with this customerId doesn''t exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        template = Template.objects.filter(customerId='system')
        template_serializer = TemplateSerializer(template, many=True)
        f = []
        for i in template_serializer.data:
            for j in i['fields']:
                f.append(j)
        t = Template(type='customer',entity='entity',customerId=str(customer_id),law='base',fields=f)
        t.save()
        td = Template.objects.filter(pk=t.id)
        tds = TemplateSerializer(td, many=True)
        if tds.data == []:
            return JsonResponse({'Message': 'The template with this customerId doesn''t exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse(tds.data, safe=False, status=status.HTTP_201_CREATED)
    return JsonResponse(TemplateSerializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)