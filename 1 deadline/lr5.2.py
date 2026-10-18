a, b, c = map(int, input("Введите три целых числа через пробел: ").split())
ab = a * b
bc = b * c
ca = c * a
a_pow4 = a ** 4
b_mod_c = b % c
c_div_a = c // a
print("a * b =", ab)
print("b * c =", bc)
print("c * a =", ca)
print("a ** 4 =", a_pow4)
print("b % c =", b_mod_c)
print("c // a =", c_div_a)
total = a_pow4 + b_mod_c + c_div_a
print("Сумма (a**4 + b%c + c//a) =", total)
#вроде так, я сидел тут часа полтора