# defining class A
class A:
    def __init__(self, txt):
        print(txt, 'I am in A Class')


# B class inheriting A
class B(A):
    def __init__(self, txt):
        super().__init__(txt)
        print(txt, 'I am in B class')


# C class inheriting B
class C(B):
    def __init__(self, txt):
        super().__init__(txt)
        print(txt, 'I am in C class')


# D class inheriting B
class D(B):
    def __init__(self, txt):
        super().__init__(txt)
        print(txt, 'I am in D class')


# E class inheriting both D and C
class E(C, D):
    def __init__(self):
        super().__init__('hello ')
        print('I am in E class')


# driver code
d = E()
