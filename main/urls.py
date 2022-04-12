from django.contrib import admin
from django.urls import include, path, re_path
from main import views as views


urlpatterns = [
    path('polling_units/results',views.PollingUnitResults.as_view(),name="polling_units_results"),
    path('polling_units/poll',views.AnnouncedPUResult.as_view(),name="polling_units_polls"),
    path('lga/results',views.LGAResults.as_view(),name="lga_results"),
    path('lga/total',views.LgaTotal.as_view(),name="lga_total"),
    path('create/poll',views.CreatePoll.as_view(),name="create_poll"),
]
