from django.shortcuts import render
from django.views.decorators.http import require_POST
from utils import restful
from django.http import HttpResponse
import os
from final import Final
#
# def index(request):
#     print("hello")
#     cwd = os.getcwd()
#     print(cwd)
#     return render(request,'index.html')

# @require_POST
# def upload_pic(request):
#     img = request.FILES.get('img')
#     name = img.name
#     with open(os.path.join(settings.MEDIA_ROOT,name),'wb') as fp:
#         for chunk in img.chunks():
#             fp.write(chunk)
#     url = request.build_absolute_uri(settings.MEDIA_URL+name)
#     return restful.result(data={'url':url})


def index(request):
    return render(request, "index.html")


def get_ajax(request):
    print("I'm in get_ajax")
    print("FIFLE", request.FILES)  # 上传文件对象
    print("POST", request.POST)
    response = {"flag": True}
    import json
    file_obj = request.FILES.get("avatar")
    print("文件名：", file_obj.name, "-----")
    with open(os.path.join('media', file_obj.name), "wb") as f:
        for i in file_obj:
            f.write(i)
    url = os.path.join('media/'+ file_obj.name)
    print(url)
    print(os.getcwd())
    results=Final.start(url,"20180408-102900")
    found_url=results[0]
    print(found_url)
    return restful.result(data={'url':found_url})

