from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> Dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        estatistica = {'dia': self.dia, 'agencia': self.agencia, 'clientes atendidos': clientes_atendidos,
                       'quantidade de clientes atendidos': len(clientes_atendidos)}
        return estatistica
