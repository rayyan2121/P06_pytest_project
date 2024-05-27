from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_sub(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_multi(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 5332114
        assert result == expected   
    def test_dev(self):
        # arrange
        a = 4
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 2
        assert result == expected