from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def dashboard(request):


    context_data = {    
        'title': 'Dashboard',
        'subtitle': 'Dashboard',
    }
    return render(request, 'dashboard.html', context_data)


def get_all_forms(request):
    mensagens = {'mensagem': '', 'tipo': ''}

    
    context_data = {
        'mensagens': mensagens
    }
    return context_data

def render_all_forms(request):

    context_data = get_all_forms(request)

    if request.method == 'POST':
        # Captura os dados do formulário
        nome = request.POST.get('valorGasto')  # Ajuste conforme necessário
        tipo_gasto = request.POST.get('tipo_gasto')
        tipo_local = request.POST.get('tipo_local')
        tipo_quem = request.POST.get('tipo_quem')
        entrada_saida = request.POST.get('entrada_saida')
        status = request.POST.get('status')
        observacao = request.POST.get('observacao')

        # Cria um novo objeto Gasto
        novo_gasto = Gasto(
            nome=nome,
            tipo_gasto=tipo_gasto,
            tipo_local=tipo_local,
            tipo_quem=tipo_quem,
            entrada_saida=entrada_saida,
            status=status,
            observacao=observacao
        )
        novo_gasto.save()  # Salva o gasto no banco de dados

        # Redireciona ou exibe uma mensagem de sucesso
        context_data['mensagens']['mensagem'] = 'Gasto adicionado com sucesso!'
        context_data['mensagens']['tipo'] = 'success'

    return render(request, 'financeiro/all_forms.html', context_data)
