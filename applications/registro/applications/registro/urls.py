from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'registro_app'

urlpatterns = [
    path('listar-todo/',
        views.DocenteListViewAll.as_view(),
         name ='listar-todo'
    ),
    path('detalle/<pk>/',
        views.DocenteDetalleView.as_view(),
        name = 'detalle'
    ),
    path('listar-Materia/',
        views.MateriaListViewAll.as_view(),
         name ='listar-Materia'
    ),
    path('listar-NoDocente/',
        views.NoDocenteListViewAll.as_view(),
         name ='listar-NoDocente'
    ),
    path('listar-Oficina/',
        views.OficinaListViewAll.as_view(),
         name ='listar-Oficina'
    ),
    path('altaO/',
        views.OficinaCreateView.as_view(),
         name ='altaO'
    ),

    path('buscar-por-apellido/',
        views.DocenteListViewAllBuscar.as_view(),
             name = 'buscar'
    ),
    path('exito/',
        views.SuccessView.as_view(),
        name = 'exito'
    ),
    path('alta/',
        views.DocenteCreateView.as_view(),
        name = 'alta'
    ),
    path('altaND/',
        views.NoDocenteCreateView.as_view(),
        name = 'altaND'
    ),
    path('modifD/<pk>/',
       views.DocenteUpdateView.as_view(),
       name = 'modifD'
    ),
    path('borrar/<pk>/',
       views.DocenteDeleteView.as_view(),
       name = 'borrar'
    ),
    path('',
       views.VistaPrincipal.as_view(),
       name = 'index'
    ),
]
