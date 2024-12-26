

##第1題
# 定義多項式 f(x) = 6x^4 + 2x^2 + 3
def f(x):
    return 6 * (x**4) + 2 * (x**2) + 3

# 儲存結果的字典格式
polynomial = {
    "coefficients": [4, 6, 0, 2, 3,0],  # 係數對應 [6x^4, 0x^3, 2x^2, 0x, 3]
    "degree": 4                       # 多項式的最高次數
}

# 計算 x = 91 時的值
x = 91
result = f(x)

# 顯示結果
print()
print(f"f({x}) = {result}")

##第2題
class Term:
    """多項式的一個單項 (如 6x^4)"""
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient  # 係數
        self.exponent = exponent        # 次方

    def evaluate(self, x):
        """計算單項的值"""
        return self.coefficient * (x ** self.exponent)


class Polynomial:
    """多項式 (如 f(x) = 6x^4 + 2x^2 + 3)"""
    def __init__(self):
        self.terms = []  # 儲存多項式中的所有單項

    def add_term(self, coefficient, exponent):
        """新增一個單項"""
        self.terms.append(Term(coefficient, exponent))

    def evaluate(self, x):
        """計算多項式的值"""
        return sum(term.evaluate(x) for term in self.terms)


# 建立多項式 f(x) = 6x^4 + 2x^2 + 3
f = Polynomial()
f.add_term(6, 4)  # 6x^4
f.add_term(2, 2)  # 2x^2
f.add_term(3, 0)  # 3 (常數項)

# 計算 x = 91 時的值
x = 91
result = f.evaluate(x)

# 顯示結果
print()
print(f"f({x}) = {result}")
