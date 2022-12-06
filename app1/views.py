from app1.models import Details
from app1.serializers import DetailsSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def course(request):
    obj1 =Details.objects.all()
    seri =DetailsSerializers(obj1,many =True)
    json_data = JSONRenderer().render(seri.data)
    return HttpResponse(json_data,content_type ='application/json')

