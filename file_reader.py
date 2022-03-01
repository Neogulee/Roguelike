import os
from typing import List, Dict
from xml.etree.ElementTree import Element, ElementTree, parse

from singleton_type import SingletonType


class FileReader(metaclass=SingletonType):
    def __init__(self):
        self.__element_dict: Dict[str, List[Element]] = {}
        self.__read_xml_dir("defs")

    def __read_xml_dir(self, dir_name: str) -> None:
        for file_name in os.listdir(dir_name):
            full_file_name: str = os.path.join(dir_name, file_name)
            ext: str = os.path.splitext(full_file_name)[-1]
            if os.path.isdir(full_file_name):
                self.__read_xml_dir(full_file_name)
            elif ext == ".xml":
                tree: ElementTree = parse(full_file_name)
                root: Element = tree.getroot()
                for element in root:
                    tag: str = element.tag
                    if tag not in self.__element_dict:
                        self.__element_dict[tag] = []
                    self.__element_dict[tag].append(element)
    
    def get_element_list(self, tag: str):
        return self.__element_dict[tag]


if __name__ == "__main__":
    file_reader = FileReader()
    element_dict = file_reader.get_element_list(tag="enemy")
    print(element_dict)