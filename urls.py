from django.urls import path
from django_filters.views import FilterView

from . import views
from .filters import RequerimentoFilter

# precisa adicionar o include no urls.py do django
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.Index.as_view(), name='index'),

    # aluno
    path('aluno/', views.AlunoList.as_view(), name='aluno_lista'),
    path('aluno/novo', views.AlunoCreate.as_view(), name='aluno_novo'),
    path('aluno/<int:pk>/', views.AlunoDetail.as_view(), name='aluno_info'),

    # requerimento genérico
    path('requerimento/<int:pk>/', views.requerimento_info, name='requerimento_info'),
    path('requerimento/', views.RequerimentoList.as_view(), name='requerimento_lista'),
    path('requerimento/busca/', FilterView.as_view(filterset_class=RequerimentoFilter), name='requerimento_busca'),
    path('requerimento/<int:pk>/parecer/', views.requerimento_parecer, name='requerimento_parecer'),

    # requerimento matrícula
    path('requerimento/matricula/novo/', views.requerimentomatricula_novo, name='requerimento_matricula_novo'),

    # protocolo avulso
    path('protav/novo/', views.protocoloavulso_novo, name='protocolo_avulso_novo'),
    path('protav/<int:pk>/', views.ProtocoloAvulsoDetail.as_view(), name='protocolo_avulso_info'),
]

#requerimento_alteracao
urlpatterns += [
    path('requerimento/alteracao/novo/', views.RequerimentoAlteracaoCreate.as_view(), name='requerimento_alteracao_novo'),
    path('requerimento/alteracao/<int:pk>/', views.RequerimentoAlteracaoDetail.as_view(), name='requerimento_alteracao_info'),
    path('requerimento/alteracao/', views.RequerimentoAlteracaoList.as_view(), name='requerimento_alteracao_lista'),
    path('requerimento/alteracao/<int:pk>/parecer/', views.RequerimentoAlteracaoUpdate.as_view(), name='requerimento_alteracao_parecer'),
]

#requerimento_boletim
urlpatterns += [
    path('requerimento/boletim/novo/', views.RequerimentoAlteracaoCreate.as_view(initial={'subtipo':'B'}), name='requerimento_boletim_novo'),
    path('requerimento/boletim/<int:pk>/', views.RequerimentoAlteracaoDetail.as_view(), name='requerimento_boletim_info'),
    path('requerimento/boletim/', views.RequerimentoAlteracaoList.as_view(), name='requerimento_boletim_lista'),
    path('requerimento/boletim/<int:pk>/parecer/', views.RequerimentoAlteracaoUpdate.as_view(initial={'subtipo':'B'}), name='requerimento_boletim_parecer'),
]

#requerimento_matricula
urlpatterns += [
    path('requerimento/matricula/<int:pk>/', views.RequerimentoMatriculaDetail.as_view(), name='requerimento_matricula_info'),
    path('requerimento/matricula/', views.RequerimentoMatriculaList.as_view(), name='requerimento_matricula_lista'),
]

#requerimento_outros
urlpatterns += [
    path('requerimento/outros/novo/', views.RequerimentoOutrosCreate.as_view(), name='requerimento_outros_novo'),
    path('requerimento/outros/<int:pk>/', views.RequerimentoOutrosDetail.as_view(), name='requerimento_outros_info'),
    path('requerimento/outros/', views.RequerimentoOutrosList.as_view(), name='requerimento_outros_lista'),
    path('requerimento/outros/<int:pk>/parecer/', views.RequerimentoOutrosUpdate.as_view(), name='requerimento_outros_parecer'),
]
