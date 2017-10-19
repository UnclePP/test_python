from django.http import HttpResponse


def index(request):
    print('hello in dev')
    print('githup网页上修改')
    return HttpResponse('土豆')
