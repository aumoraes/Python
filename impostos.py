# -*- coding: UTF-8 -*-
# impostos.py
#usado para python versao < 3
#from abc import ABCMeta, abstractmethod
import abc


class Imposto(metaclass=abc.ABCMeta):
    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abc.abstractmethod
    def calcula(self, orcamento):
        pass

class Template_de_imposto_condicional(Imposto):

    #Essa atribuicao torna a classe abstrata
    #__metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deveria_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
        else:
           return self.minima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)

    #Essa anotacao torna o metodo obrigado de ser implementado
    # por quem herda

    @abc.abstractmethod
    def deveria_usar_maxima_taxacao(self, orcamento):
        pass

    @abc.abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abc.abstractmethod
    def minima_taxacao(self, orcamento):
        pass

class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)


def selic(metodo_ou_funcao):
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50
    return wrapper

class ISS(Imposto):
    @selic
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)

class IPVA(Template_de_imposto_condicional):

    def deveria_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

class IPTU(Template_de_imposto_condicional):

    def deveria_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.10

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self,orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True

        return False

