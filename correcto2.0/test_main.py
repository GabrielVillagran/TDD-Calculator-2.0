import pytest 
from main import *
#multiple validacion de datos en suma
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (3,2,5),
        (2,3,5),
        (suma(3,2), 5, 10),
        (3, suma(2,5), 10)
    ]
)
def test_suma_multi(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected
#multiple validacion de datos en resta
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (2,1,1),
        (-2,-5, 3),
        (-2, 7, -9),
        (10, -6, 16)
    ]
)
def test_resta_multi(input_a, input_b, expected):
    assert resta(input_a, input_b) == expected
#multiple validacion de datos en multiplicacion
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (2,1,2),
        (-2,-2, 4),
        (-2, 2, -4)
    ]
)
def test_multiplicacion_multi(input_a, input_b, expected):
    assert multipli(input_a, input_b) == expected
#multiple validacion de datos en division
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (4,2,2),
        (-4,-2, 2),
        (-4, 2, -2),
        (0, 10, 0)
    ]
)
def test_division_multi(input_a, input_b, expected):
    assert divi(input_a, input_b) == expected
#multiple validacion de datos en exponente
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (2,2,4),
        (-2,2, 4),
        (-2, 3, -8),
        (0, 10, 0),
        (1,0,1)
    ]
)
def test_exponente_multi(input_a, input_b, expected):
    assert exp(input_a, input_b) == expected
#multiple validacion de datos en cuadratica
@pytest.mark.parametrize(
    "input_a, input_b, input_c, expected",
    [
        (1,-2, 1, 1)
    ]
)
def test_cuadratica_multi(input_a, input_b, input_c, expected):
    assert cuadratica(input_a, input_b, input_c) == expected