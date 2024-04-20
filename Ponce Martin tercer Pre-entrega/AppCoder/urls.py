from django.urls import path

from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('buscar/', views.buscar),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("elimina_estudiante/<int:id>" , views.elimina_estudiante , name="elimina_estudiante"),
    path("editar_estudiante/<int:id>" , views.editar , name="editar_estudiante"),
    path("elimina_profesor/<int:id>" , views.elimina_profesor , name="elimina_profesor"),
    path("editar_profesor/<int:id>" , views.editar , name="editar_profesor")
    
   
]

