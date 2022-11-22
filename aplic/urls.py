from django.urls import path

from .views import IndexView, SobreView, DadosGraficoAlunosView
from .views import ProfessoresView
from .views import CursoDetalheView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('professores/', ProfessoresView.as_view(), name='professores'),
    path('curso/<int:id>/', CursoDetalheView.as_view(), name='curso'),
    path('dados-grafico-alunos/', DadosGraficoAlunosView.as_view(), name='dados-grafico-alunos'),


]