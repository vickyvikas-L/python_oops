class A:
    def __init__(self):
        print("Constructor of A")


class B:
    def __init__(self):
        print("Constructor of B")


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Constructor of C")


obj = C()