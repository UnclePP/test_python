from django.http import HttpResponse


def index(request):
    print('add this line in uncle')
    print('githup网页上修改')
    return HttpResponse('土豆')
