from enum import auto, Enum
from typing import Callable, Dict, List

from singleton_type import SingletonType


# FIX

class Event(Enum):
    DEAD = auto()
    KILL = auto()


def listener_function(event: Event):
    def decorator(func):
        EventManager().append_listener(event, func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return decorator

class EventManager(metaclass=SingletonType):
    def __init__(self):
        self.__listener_dict: Dict[List[Callable]] = {}
    
    def append_listener(self, event: Event, callback: Callable) -> None:
        if event not in self.__listener_dict:
            self.__listener_dict[event]: List[Callable] = []
        self.__listener_dict[event].append(callback)
    
    def remove_listener(self, event: Event, callback: Callable):
        pass
    
    def post_notification(self, event: Event, **kwargs) -> None:
        if event not in self.__listener_dict:
            return            
        for listener in self.__listener_dict[event]:
            parameters = dict.fromkeys(listener.__code__.co_varnames, None)
            for key, val in kwargs.items():
                if key in parameters:
                    parameters[key] = val
            listener(**parameters)
    
    def test(self):
        print(self.__listener_dict)


if __name__ == "__main__":
    event_manager = EventManager()
    def test_callback(*args, **kwargs):
        print("ASDF")
    
    @listener_function(Event.DEAD)
    def test1():
        print("test1")

    @listener_function(Event.DEAD)
    def test2(name):
        print("test2: ", name)

    @listener_function(Event.DEAD)
    def test3(name, asdf):
        print("test3: ", name, ", asdf: ", asdf)
    
    @listener_function(Event.KILL)
    def test4(target):
        print("target: ", target)

    class TestClass:
        def __init__(self):
            self.a = 3

        @classmethod
        @listener_function(Event.DEAD)
        def asdf(self, asdf):
            # print("a: ", self.a)
            print("self: ", self)
            print("test_class: ", asdf)

        def qwer(self):
            print(self.a)
            
    event_manager.append_listener(Event.DEAD, test_callback)
    test_class = TestClass()
    test_class.qwer()
    test_class.asdf("zxcv")
    print("-----Event Dead-----")
    event_manager.post_notification(Event.DEAD, name="zxcv", asdf="zz")
    print("-----Event Kill-----")
    event_manager.post_notification(Event.KILL, name="zxcv", asdf="zz")
