"""
Simple json generator with complexity possibilities
"""
from __future__ import annotations
import json


class ConfJson:
    """
    Json Object config
    """

    def __init__(self, nb_string,
                 nb_obj=0, size_obj_1=0,
                 nb_json=0, conf_json=None,
                 nb_list: int = 0, nb_list_elements: int = 0, conf_list_json: ConfJson = None):
        """
        Json Object config
        :param nb_string:
        :param nb_obj:
        :param size_obj_1:
        :param nb_json:
        :param conf_json:
        """
        self.nb_string = nb_string
        self.nb_obj = nb_obj
        self.size_obj_1 = size_obj_1
        self.nb_json = nb_json
        self.conf_json = conf_json
        self.nb_list = nb_list
        self.conf_list_json = conf_list_json
        self.nb_list_elements = nb_list_elements


class JsonElement:

    @property
    def json_dict(self):
        raise NotImplementedError


class JsonString(JsonElement):

    def __init__(self, prefix: int or str, number: int, index: int, list_index: int = None):
        self.prefix = str(prefix)
        self.number = number
        self.index = index
        self.list_index = list_index

    @property
    def json_dict(self):

        key = f"{self.prefix}-{self.number}"

        if self.list_index is None:
            value = f"{self.prefix}{self.number}.{self.index}"
        else:
            value = f"{self.prefix}{self.number}L{self.list_index}.{self.index}"

        new_dict = {key: value}
        return new_dict


class JsonObj(JsonElement):

    def __init__(self, prefix: int or str, number: int, index: int, nbr_inside_list: int):
        self.prefix = str(prefix)
        self.number = number
        self.index = index
        self.nbr_inside_obj = nbr_inside_list

    @property
    def json_dict(self):
        key = f"{self.prefix}-{self.number}"
        value = JsonGenerator(f"{self.prefix}{self.number}", self.nbr_inside_obj).json_dict
        new_dict = {key: value}
        return new_dict


class JsonGenerator:

    def __init__(self, name,
                 nb_string: int,
                 nb_obj: int = 0, size_obj_1: int = 0,
                 nb_json: int = 0, conf_json: ConfJson = None,
                 nb_list: int = 0, nb_list_elements: int = 0, conf_list_json: ConfJson = None,
                 list_index: int = None):
        self.name = str(name)
        self.nb_string = nb_string
        self.nb_obj = nb_obj
        self.size_list_1 = size_obj_1
        self.nb_json = nb_json
        self.conf_json = conf_json
        self.nb_list = nb_list
        self.conf_list_json = conf_list_json
        self.nb_list_elements = nb_list_elements
        self.list_index = list_index

    @property
    def json_dict(self):
        if self.list_index is None:
            id_value = f"{self.name}"
        else:
            id_value = f"{self.name}L{self.list_index}"

        final_json_dict = {"id": id_value}
        index = 0
        for _ in range(self.nb_string):
            index += 1
            final_json_dict.update(JsonString(self.name, index, index,
                                              list_index=self.list_index).json_dict)
        for _ in range(self.nb_obj):
            index += 1
            final_json_dict.update(JsonObj(self.name, index, index,
                                           self.size_list_1).json_dict)
        for _ in range(self.nb_json):
            index += 1
            new_json = JsonGenerator(f"{self.name}{index}",
                                     self.conf_json.nb_string,
                                     self.conf_json.nb_obj, self.conf_json.size_obj_1,
                                     self.conf_json.nb_json, self.conf_json.conf_json,
                                     list_index=self.list_index).json_dict

            key = f"{self.name}-{index}"
            value = new_json
            new_dict = {key: value}
            final_json_dict.update(new_dict)

        for _ in range(self.nb_list):
            index += 1
            list_of_json = []
            for list_index in range(self.nb_list_elements):
                new_json = JsonGenerator(f"{self.name}{index}",
                                         self.conf_list_json.nb_string,
                                         self.conf_list_json.nb_obj, self.conf_list_json.size_obj_1,
                                         self.conf_list_json.nb_json, self.conf_list_json.conf_json,
                                         list_index=list_index).json_dict
                list_of_json.append(new_json)
            key = f"{self.name}-{index}"
            new_dict = {key: list_of_json}
            final_json_dict.update(new_dict)

        return final_json_dict

    def generate_json_file(self, path: str):
        with open(path, mode='w', encoding='utf8') as file_handler:
            file_handler.write(json.dumps(self.json_dict))


if __name__ == '__main__':
    # 1 level
    my_json = JsonGenerator(name=1,
                            nb_string=0,
                            nb_json=2, conf_json=ConfJson(3))
    my_json.generate_json_file("json_objects_1_levels.json")

    # 2 level
    my_json = JsonGenerator(name=1,
                            nb_string=2,
                            nb_obj=2, size_obj_1=3,
                            nb_json=3, conf_json=ConfJson(2, 2, 2))
    my_json.generate_json_file("json_objects_2_levels.json")

    # 3 level
    my_json = JsonGenerator(name=2,
                            nb_string=2,
                            nb_obj=2, size_obj_1=3,
                            nb_json=3, conf_json=ConfJson(2, 2, 2,
                                                          1, ConfJson(1, 2, 2)))
    my_json.generate_json_file("json_objects_3_levels.json")

    # only one list
    my_json = JsonGenerator(name=2,
                            nb_string=0,
                            nb_obj=0,
                            nb_json=0,
                            nb_list=1, nb_list_elements=2, conf_list_json=ConfJson(nb_string=3))
    my_json.generate_json_file("json_only_one_list.json")

    # only one list
    my_json = JsonGenerator(name=2,
                            nb_string=0,
                            nb_obj=0,
                            nb_json=0,
                            nb_list=1, nb_list_elements=2,
                            conf_list_json=ConfJson(nb_string=3,
                                                    nb_obj=2, size_obj_1=2,
                                                    nb_json=2, conf_json=ConfJson(5),
                                                    nb_list=1, nb_list_elements=5, conf_list_json=ConfJson(nb_string=3)))

    my_json.generate_json_file("json_double_list.json")
