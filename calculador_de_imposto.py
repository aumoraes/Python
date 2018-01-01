# -*- coding: UTF-8 -*-
# calculador_de_imposto.py

class Calculador_de_imposto(object):
    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula( orcamento )
        print(valor)

if __name__ == "__main__":

    from impostos import *
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item("Item A", 100.0))
    orcamento.adiciona_item(Item("Item B", 50.0))
    orcamento.adiciona_item(Item("Item C", 400.0))

    #orcamento = Orcamento(500.00)
    print("Valor do orcamento: R$", orcamento.valor)
    calculador_de_imposto = Calculador_de_imposto()
    print("Calculo do ISS usando o decorator: ", end="")
    calculador_de_imposto.realiza_calculo(orcamento, ISS())
    print("Calculo do ICMS: ", end="")
    calculador_de_imposto.realiza_calculo(orcamento, ICMS())

    print("Calculo do ICMS + ISS: ", end="")
    calculador_de_imposto.realiza_calculo(orcamento, ICMS(ISS()))

    print("Calculo do IPVA: ", end="")
    calculador_de_imposto.realiza_calculo(orcamento, IPVA())
    print("Calculo do IPTU: ", end="")
    calculador_de_imposto.realiza_calculo(orcamento, IPTU())

    print("Calculo do IPTU + IPVA: ", end="")
    calculador_de_imposto.realiza_calculo(orcamento, IPTU(IPVA()))
