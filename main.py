from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


'''from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

fila_teste = FilaNormal()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_clientes(5))
print(fila_teste.chama_clientes(7))

fila_teste1 = FilaPrioritaria()
fila_teste1.atualiza_fila()
fila_teste1.atualiza_fila()
fila_teste1.atualiza_fila()
print(fila_teste1.chama_clientes(4))
print(fila_teste1.chama_clientes(6))
print(fila_teste1.estatistica('10/11/2022', 1435, 'detail'))'''

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_clientes(8))
print(teste_fabrica.chama_clientes(3))
print(teste_fabrica.chama_clientes(5))
print(teste_fabrica.estatistica(EstatisticaResumida('03/02/2020', 456)))
print(teste_fabrica.estatistica(EstatisticaDetalhada('03/02/2020', 456)))


''' Estatistica em Fila Prioritária salvo para consulta!

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
    estatistica: Dict[str, Union[List[str], str, int]] = {}
    if flag != 'detail':
        estatistica[f'{agencia} - {dia}'] = len(self.clientes_atendidos)
    else:
        estatistica = {'dia': dia, 'agencia': agencia, 'clientes atendidos': self.clientes_atendidos,
                       'quantidade de clientes atendidos': len(self.clientes_atendidos)}
    return estatistica'''