from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from app1 import models

# Create your views here.

def add_record_handler(request):
    if request.method == 'GET':
        return render(request, 'add_object_.html')
    else:
        good_to_add = models.Goods(name=request.POST['good'], description=request.POST['description'])
        good_to_add.save()
        count = models.Goods.objects.count()
        return JsonResponse({'status': 'ok', 'objects_in_db': count, 'added_object': good_to_add.id})

def get_record_handler(request, object_id):
    requested_good = models.Goods.objects.get(id=object_id)
    return JsonResponse({'status': 'ok', 'data': model_to_dict(requested_good)})