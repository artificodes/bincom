from enum import unique
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView,View
from rest_framework.response import Response
# Create your views here.
from .models import *
from .serializers import *
from rest_framework import generics,viewsets,status


class PollingUnitResults(APIView):
    queryset = PollingUnit.objects.all()
    serializer_class = PollingUnitSerializer

    def get(self,request):
        template = 'main/polling_results_page.html'
        polling_units =PollingUnit.objects.all()
        context = {}
        context['units'] = polling_units
        return render(request,template,context)



class LGAResults(APIView):
    queryset = Lga.objects.all()
    serializer_class = LGAsSerializer

    def get(self,request):
        template = 'main/lga_results_page.html'
        lgas =Lga.objects.all()

        context = {}
        context['lgas'] = lgas
        return render(request,template,context)



class AnnouncedPUResult(APIView):
    queryset = AnnouncedPuResults.objects.all()
    serializer_class = AnnouncedPollingUnitSerializer

    def get(self,request):
        template = 'main/results.html'
        uniqueid = request.GET.get('uniqueid')
        polling_unit = PollingUnit.objects.get(uniqueid=uniqueid)
        polling_unit_serialized = PollingUnitSerializer(polling_unit).data
        polling_unit_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid = uniqueid)
        polling_unit_results_serialized = AnnouncedPollingUnitSerializer(polling_unit_results,many=True).data
        data = {'polling_unit':polling_unit_serialized,'polls':polling_unit_results_serialized}
        return Response(data,status=200)



class LgaTotal(APIView):
    queryset = Lga.objects.all()
    serializer_class = LGAsSerializer

    def get(self,request):
        lga_id = request.GET.get('lga_id')
        lga = Lga.objects.get(lga_id=lga_id)
        lga_serialized = LGAsSerializer(lga).data
        polling_units = PollingUnit.objects.filter(lga_id=lga.lga_id)
        total = 0
        for unit in polling_units:
            polling_unit_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid = unit.uniqueid)
            for result in polling_unit_results.all():
                total+=result.party_score
        data = {'total':total,'lga':lga_serialized,}
        return Response(data,status=200)



class CreatePoll(generics.CreateAPIView):
    queryset = AnnouncedPuResults.objects.all()
    serializer_class = AnnouncedPollingUnitSerializer

    # def get(self,request):
    #     template = 'main/results.html'
    #     uniqueid = request.GET.get('uniqueid')
    #     polling_unit = PollingUnit.objects.get(uniqueid=uniqueid)
    #     polling_unit_serialized = PollingUnitSerializer(polling_unit).data
    #     polling_unit_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid = uniqueid)
    #     polling_unit_results_serialized = AnnouncedPollingUnitSerializer(polling_unit_results,many=True).data
    #     data = {'polling_unit':polling_unit_serialized,'polls':polling_unit_results_serialized}
    #     return Response(data,status=200)


