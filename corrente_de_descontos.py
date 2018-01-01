# -*- coding: UTF-8 -*-
# corrente_de_descontos.py

from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Corrente_de_descontos(object):
    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        )

        return desconto.calcula(orcamento)

if __name__ == "__main__":

    from orcamento import Orcamento, Item
    orcamento = Orcamento()
    orcamento.adiciona_item(Item("Item A", 100.0))
    orcamento.adiciona_item(Item("Item B", 50.0))
    orcamento.adiciona_item(Item("Item C", 400.0))
    print("Valor do orcamento: R$", orcamento.valor)


    calculador_de_descontos = Corrente_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print("Desconto calculado:  %6.2f" %(desconto))