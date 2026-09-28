def mdc(a: int, b: int) -> int:
    if b == 0:
        return a
    return mdc(b, a % b)

def soma_digitos(n: int) -> int:
    if n < 10:
        return n
    return (n % 10) + soma_digitos(n // 10)