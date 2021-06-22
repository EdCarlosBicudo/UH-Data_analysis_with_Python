from decimal import Decimal

class Rational(object):
    def __init__(self, r1, r2):
        self.r1 = float(r1)
        self.r2 = float(r2)
        self.value = float(r1).__truediv__(float(r2)).__round__(4)

    def __float__(self):
        return float(self.value).__round__(4)

    def __add__(self, x):
        return self.value.__add__(x.__float__()).__round__(4)

    def __sub__(self, x):
        return self.value.__sub__(x.__float__()).__round__(4)

    def __mul__(self, x):
        return self.value.__mul__(x.__float__()).__round__(4)

    def __truediv__(self, x):
        return self.value.__truediv__(x.__float__()).__round__(4)

    def __floordiv__(self, x):
        return self.value.__floordiv__(x.__float__()).__round__(4)

    def __eq__(self, x):
        return self.value == x.__float__()

    def __ge__(self, x):
        return self.value >= x.__float__()

    def __gt__(self, x):
        return self.value > x.__float__()

    def __le__(self, x):
        return self.value <= x.__float__()

    def __lt__(self, x):
        return self.value < x.__float__()

    def __ne__(self, x):
        return self.value != x.__float__()

    def __str__(self):
        return f"{self.r1}/{self.r2}"

    def __repr__(self):
        return f"{float(self.value):.4f}"

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
