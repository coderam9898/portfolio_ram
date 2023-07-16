from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def index(request):
    template  = loader.get_template('main/index.html')
    # return HttpResponse('helloworld')
    # return render(request, 'hello.html', {})
    return HttpResponse(template.render({},request))