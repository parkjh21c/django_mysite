from django.http import HttpResponse

def index(request):
  return HttpResponse("안녕하세요")

# Create your views here.
