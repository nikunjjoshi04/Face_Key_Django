from django.shortcuts import render
from django.views.generic import TemplateView
import cv2 as cv
from django.http import JsonResponse
import numpy as np
from django.core.serializers import serialize
import json
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'detection/index.html'

    def get(self, request, *args, **kwargs):
        return super(HomePageView, self).get(request, *args, **kwargs)


def img(request):
    img1 = list(request.GET['image'])
    print(img1)
    print(type(img1))
    return JsonResponse({'data': "AJAX_RESPONSE"})


def video_ajax(request):
    img = cv.imread('static/images/nikunj.jpg')
    cv.namedWindow("Hrithik", cv.WINDOW_NORMAL)
    cv.imshow('Hrithik', img)

    cv.waitKey(2000)
    cv.destroyAllWindows()

    return JsonResponse({'data': 'AJAX_RESPONSE'})
