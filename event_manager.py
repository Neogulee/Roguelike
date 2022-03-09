from enum import auto, Enum
from functools import wraps
from typing import Callable, Dict, List

from singleton_type import SingletonType


class Event(Enum):
    DEAD = auto()
    KILL = auto()


class EventManager(metaclass=SingletonType):
    def __init__(self):
        self.__listener_dict: Dict[List[Callable]] = {}
    
    def append_listener(self, event: Event, callback: Callable) -> None:
        if event not in self.__listener_dict:
            self.__listener_dict[event]: List[Callable] = []
        self.__listener_dict[event].append(callback)
    
    def remove_listener(self, event: Event, callback: Callable) -> None:
        if event not in self.__listener_dict:
            raise
        self.__listener_dict[event].remove(callback)
    
    def post_notification(self, event: Event, **kwargs) -> None:
        if event not in self.__listener_dict:
            return
        for listener in self.__listener_dict[event]:
            varnames: List[str]
            if hasattr(listener, "varnames"):
                varnames = listener.varnames
            else:
                varnames = listener.__code__.co_varnames
            
            parameters = dict.fromkeys(varnames, None)
            parameters.pop("self", None)
            
            for key, val in kwargs.items():
                if key in parameters:
                    parameters[key] = val
            
            listener(**parameters)

    def print_listener_dict(self) -> None:
        print(self.__listener_dict)


def listener_function(*events: Event):
    def decorator(func):
        for event in events:
            EventManager().append_listener(event, func)
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return decorator

    
def listener_method(*events: Event):
    def decorator(func):
        func.listener_events = events
        func.varnames = func.__code__.co_varnames
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return decorator


class ListenerMeta(type):
    def __new__(cls, name, bases, dct):
        event_manager = EventManager()

        listener_list = []
        inner_init = dct.get("__init__", None)
        def __init__(self, *args, **kwargs):
            attrbute_list = [getattr(self, name) for name in dir(self)]
            method_list = [method for method in attrbute_list if callable(method)]
            for method in method_list:
                listener_events = getattr(method, "listener_events", None)
                if listener_events is not None:
                    for event in listener_events:
                        event_manager.append_listener(event=event, callback=method)
                    listener_list.append(method)
            if inner_init is not None:
                inner_init(self, *args, **kwargs)
        dct["__init__"] = __init__

        inner_del = dct.get("__del__", None)
        def __del__(*args, **kwargs):
            for listener in listener_list:
                listener_events = getattr(listener, "listener_events", None)
                for event in listener_events:
                    event_manager.remove_listener(event=event, callback=listener)
            if inner_del is not None:
                inner_del(*args, **kwargs)
        dct["__del__"] = __del__
        
        new_cls = super().__new__(cls, name, bases, dct)
        return new_cls


if __name__ == "__main__":
    event_manager = EventManager()  
    
    class ASDF(metaclass=ListenerMeta):
        def __init__(self):
            self.a = 1
            pass

        def zxcv(self):
            print("QWER")

        @listener_method(Event.DEAD)
        def asdf(self):
            print(self.a, "vvd")

        @listener_method(Event.DEAD, Event.KILL)
        def foo(self, bar, dqwe):
            print(bar, dqwe)

    @listener_function(Event.DEAD, Event.KILL)
    def test_function(bar, zz):
        print("test:", bar, zz)
        
    asdf = ASDF()
    print("----------DEAD----------")
    event_manager.post_notification(Event.DEAD, bar="zx")
    print("----------KILL----------")
    event_manager.post_notification(Event.KILL, dqwe=123)
