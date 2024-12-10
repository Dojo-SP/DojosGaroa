from collections.abc import Sequence
import pytest


def daytrade(serie: Sequence[int]) -> int:
    res = 0
    mini = serie[0] if serie else None
    for item in serie:
        if item < mini:
            mini = item
        elif (valor := item - mini) > res:
            res = valor
    return res


@pytest.mark.parametrize("serie, expected", [
    ([100, 105], 5),
    ([102, 105], 3),
    ([105, 100], 0),
    ([105], 0),
    ([], 0),
    ([100, 105, 110], 10),
    ([100, 105, 100], 5),
    ([105, 100, 110], 10),
    ([105, 100, 110, 100], 10),
    ([105, 100, 109, 100], 9),
    ([105, 109, 100, 100], 4),
    ([99, 100, 110, 100], 11),
    ([100, 110, 100, 110], 10),
    ([100, 105, 100, 110], 10),
    ([100, 105, 100, 105], 5),
    ([100, 104, 100, 105], 5),
    (range(5001), 5000),
])
def test_mapeia_entrada_saida(serie, expected):
    assert daytrade(serie) == expected
