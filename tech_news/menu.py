# Requisitos 11 e 12
import sys
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
from tech_news.scraper import get_tech_news


def sair():
    print("Encerrando script")
    # sys.stdin.close()


options = {
    "0": (get_tech_news, True, "Digite quantas notícias serão buscadas:"),
    "1": (search_by_title, True, "Digite o título:"),
    "2": (search_by_date, True, "Digite a data no formato aaaa-mm-dd:"),
    "3": (search_by_category, True, "Digite a categoria:"),
    "4": (top_5_categories, False, ""),
    "5": (sair, False, ""),
}


def analyzer_menu():
    option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair."""
    )
    if option not in options:
        return sys.stderr.write("Opção inválida\n")

    function, needs_input, input_text = options[option]
    try:
        if needs_input:
            param = input(input_text)
            return function(param)
        else:
            return function()
    except Exception:
        print("Opção inválida", file=sys.stderr)


# print(analyzer_menu())
