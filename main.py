"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    if len(numbers) < 2:
        return None
    
    primeiro = numbers[0]  # o primeiro número da soma
    segundo = numbers[1]  # o segundo número da soma
    soma = numbers[0] + numbers[1]

    for i in range(len(numbers)-1):
        for j in range(i, len(numbers)):
            if i != j:
                primeirotest = numbers[i]
                segundotest = numbers[j]
                somatest = primeirotest + segundotest
                if (somatest > soma):
                    primeiro = primeirotest
                    segundo = segundotest
                    soma = somatest
    
    if (primeiro > segundo):
        aux = primeiro
        primeiro = segundo
        segundo = aux
    
    return primeiro, segundo
