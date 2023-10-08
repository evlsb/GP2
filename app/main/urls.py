from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('add', views.add, name='add_sensor'),
    path('add_engunits', views.add_engunits, name='add_engunits'),
    path('add_cat', views.add_cat, name='add_cat'),
    path('<int:pk>', views.SensorDetailView.as_view(), name='sensor-detail'),
    path('<int:pk>/update', views.SensorUpdateView.as_view(), name='sensor-update'),
    path('<int:pk>/catupdate', views.CategoryUpdateView.as_view(), name='category-update'),
    path('<int:pk>/engupdate', views.EngUpdateView.as_view(), name='eng-update'),
    path('<int:pk>/delete', views.SensorDeleteView.as_view(), name='sensor-delete'),
    path('<int:pk>/catdelete', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('<int:pk>/engdelete', views.EngDeleteView.as_view(), name='eng-delete'),
]