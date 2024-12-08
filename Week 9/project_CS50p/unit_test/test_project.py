from project import get_list
from project import check_meat
from project import get_meat
import pytest


def test_get_list():
    with pytest.raises(ValueError):
        get_list(" ")
    with pytest.raises(ValueError):
        get_list("1")
    with pytest.raises(ValueError):
        get_list("Vegetables")
    with pytest.raises(ValueError):
        get_list("Carbohydrates")


def test_check_meat():
    assert check_meat("1") == False
    assert check_meat("") == False
    assert check_meat("123") == False
    assert check_meat("apples") == False
    assert check_meat("bananas") == False
    assert check_meat("cabbage") == False


def test_get_meat():
    assert get_meat("bison") == {"Name": "Bison", "Calories(Kcal)": "180", "Proteins(g)": "26", "Fat(g)": "9",
                                 "Saturated fats(g)": "3.5", "Monounsaturated fats(g)": "3.3", "Polyunsaturated fats(g)": "0.4"}
    assert get_meat("beef") == {"Name": "Beef", "Calories(Kcal)": "230", "Proteins(g)": "29", "Fat(g)": "12",
                                "Saturated fats(g)": "4.8", "Monounsaturated fats(g)": "5.1", "Polyunsaturated fats(g)": "0.4"}
