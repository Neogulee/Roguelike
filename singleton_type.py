class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


if __name__ == "__main__":
    class TestClass(metaclass=SingletonType):
        pass
    
    class TestClass2:
        pass
    
    class TestClass3(TestClass):
        pass

    a = TestClass()
    b = TestClass()
    c = TestClass2()
    d = TestClass2()
    e = TestClass3()
    f = TestClass3()
    print(a is b)
    print(c is d)
    print(e is f)
    print(a is e)