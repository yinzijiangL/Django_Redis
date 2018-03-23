from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template import loader


def index(request):

    # datas = {
    #     'name': 'django',
    #     'sex': '男',
    #     'age': 25,
    #     'salary': 10000,
    #     'hobby': ['python', 'c/c++', 'java']
    # }
    # template = loader.get_template("index.html")
    # html = template.render(datas,request)
    path = request.path
    method = request.method
    encoding = request.encoding

    text = "path:%s method:%s encoding:%s" %(path,method,encoding)
    return HttpResponse(text)


def show_news(request, a, b):

    text = "news:%s %s" %(a,b)
    return HttpResponse(text)


def show_news2(request, category, page_no):
    # key words parameter transfer
    text = "news2:%s %s" %(category,page_no)
    return HttpResponse(text)


def post(request):

    return render(request,"post.html")


def do_post(request):

    rqdict = request.POST

    username = rqdict.get("username")
    password = rqdict.get("password")
    gender = rqdict.get("gender")
    hobby = rqdict.getlist("hobby")
    text = "username: %s <br/>" \
           "password: %s <br/>" \
           "gedner: %s <br/>" \
           "hobby: %s <br/>" %(username,password,gender,hobby)

    return HttpResponse(text)


def test_redirect(request):

    return HttpResponseRedirect("index")


def get_json(request):
    return render(request,"get_json.html")


def do_json(request):
    data = {
        "name": "张三",
        "age": 20,
        "sex": "男",
        "salary": 999.99,

    }

    return JsonResponse(data)