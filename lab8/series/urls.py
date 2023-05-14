from django.urls import path

from . import views

urlpatterns = [
    #SERIE
    path('',views.IndexView.as_view(),name='index'),
    path('serie',views.SeriesView.as_view(),name='series'),
    path('serie/<int:serie_id>',views.SerieDetailView.as_view()),
    #PRODUCTO
    path('producto',views.ProductoView.as_view(),name='producto'),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view()),

     #CATEGORIA
    path('categoria',views.CategoriaView.as_view(),name='categoria'),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view())
]
