from django.shortcuts import render, get_object_or_404
from .models import MyappInstituicao

def home(request):
    page_number = int(request.GET.get('page', 1))
    items_per_page = 20
    start_index = (page_number - 1) * items_per_page
    end_index = start_index + items_per_page

    all_bancos = MyappInstituicao.objects.all()

    bancos = all_bancos[start_index:end_index]

    total_pages = (all_bancos.count() + items_per_page - 1) // items_per_page

    codigo_compensacao = request.GET.get('codigocompensacao')
    banco = None
    mensagem = None
    if codigo_compensacao:
        try:
            banco = MyappInstituicao.objects.get(codigocompensacao=codigo_compensacao)
        except MyappInstituicao.DoesNotExist:
            mensagem = f'Nenhum banco encontrado com o código de compensação {codigo_compensacao}.'

    return render(request, 'index.html', {
        'bancos': bancos,
        'current_page': page_number,
        'total_pages': total_pages,
        'banco': banco,
        'mensagem': mensagem
    })



