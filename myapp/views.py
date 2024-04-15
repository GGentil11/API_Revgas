from django.shortcuts import render, get_object_or_404
from .models import MyappInstituicao

def home(request):
    # Obtemos o número da página a partir do parâmetro 'page' na query string
    page_number = int(request.GET.get('page', 1))
    items_per_page = 20
    start_index = (page_number - 1) * items_per_page
    end_index = start_index + items_per_page

    # Consulta para buscar todos os bancos
    all_bancos = MyappInstituicao.objects.all()

    # Selecionamos os bancos para a página atual
    bancos = all_bancos[start_index:end_index]

    # Calculamos o número total de páginas
    total_pages = (all_bancos.count() + items_per_page - 1) // items_per_page

    # Lógica para obter detalhes do banco se um código de compensação for fornecido
    codigo_compensacao = request.GET.get('codigocompensacao')
    banco = None
    mensagem = None
    if codigo_compensacao:
        try:
            banco = MyappInstituicao.objects.get(codigocompensacao=codigo_compensacao)
        except MyappInstituicao.DoesNotExist:
            mensagem = f'Nenhum banco encontrado com o código de compensação {codigo_compensacao}.'

    # Renderizamos o template com os dados necessários
    return render(request, 'index.html', {
        'bancos': bancos,
        'current_page': page_number,
        'total_pages': total_pages,
        'banco': banco,
        'mensagem': mensagem
    })



