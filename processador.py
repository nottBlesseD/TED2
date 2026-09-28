from central_recursiva.excecoes import OperacaoInvalidaError, EntradaInvalidaError
from central_recursiva.operacoes import mdc, soma_digitos

def processar_operacao(linha: str) -> str:
    partes = linha.strip().split()
    if not partes:
        raise OperacaoInvalidaError()

    op = partes[0]

    if op not in ('M', 'S'):
        raise OperacaoInvalidaError()

    if op == 'M':
        if len(partes) != 3:
            raise EntradaInvalidaError()
        try:
            a = int(partes[1])
            b = int(partes[2])
        except ValueError:
            raise EntradaInvalidaError()

        if a <= 0 or b <= 0:
            raise EntradaInvalidaError()

        return f"MDC = {mdc(a, b)}"

    elif op == 'S':
        if len(partes) != 2:
            raise EntradaInvalidaError()
        try:
            n = int(partes[1])
        except ValueError:
            raise EntradaInvalidaError()

        if n < 0:
            raise EntradaInvalidaError()

        return f"SOMA = {soma_digitos(n)}"