from django.shortcuts import render
from django.views.generic import TemplateView
import cv2 as cv
from django.http import JsonResponse

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'detection/index.html'

    def get(self, request, *args, **kwargs):
        # print('Home')
        img = cv.imread('static/images/nikunj.jpg')
        # print(img)
        return super(HomePageView, self).get(request, *args, **kwargs)


def img(request):
    img1 = list(request.GET['image'])
    print(img1)
    print(type(img1))
    return JsonResponse({'id': 22})
