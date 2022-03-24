"""
Simple json generator with complexity possibilities
"""
import json


class ConfJson:
    def __init__(self, nb_string,
                 nb_obj=0, size_obj_1=0,
                 nb_json=0, conf_json=None):
        self.nb_string = nb_string
        self.nb_obj = nb_obj
        self.size_obj_1 = size_obj_1
        self.nb_json = nb_json
        self.conf_json = conf_json


class JsonElement:

    @property
    def json_dict(self):
        raise NotImplementedError


class JsonString(JsonElement):

    def __init__(self, prefix: int or str, number: int, index: int):
        self.prefix = str(prefix)
        self.number = number
        self.index = index

    @property
    def json_dict(self):
        key = f"{self.prefix}-{self.number}"
        value = f"{self.prefix}{self.number}.{self.index}"
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


class JsonList(JsonElement):

    def __init__(self, prefix: int or str, number: int, nbr_inside_list: int):
        self.prefix = str(prefix)
        self.number = number
        self.index = 0
        self.nbr_inside_list = nbr_inside_list

    @property
    def json_dict(self):
        key = f"{self.prefix}-{self.number}"
        value = JsonGenerator(f"{self.prefix}{self.number}", self.nbr_inside_list).json_dict
        new_dict = {key: value}
        return new_dict


class JsonGenerator:

    def __init__(self, name,
                 nb_string,
                 nb_obj=0, size_obj_1=0,
                 nb_json=0, conf_json: ConfJson = None):
        self.name = str(name)
        self.nb_string = nb_string
        self.nb_obj = nb_obj
        self.size_list_1 = size_obj_1
        self.nb_json = nb_json
        self.conf_json = conf_json

    @property
    def json_dict(self):
        final_json_dict = {"id": self.name}
        index = 0
        for _ in range(self.nb_string):
            index += 1
            final_json_dict.update(JsonString(self.name, index, index).json_dict)
        for _ in range(self.nb_obj):
            index += 1
            final_json_dict.update(JsonObj(self.name, index, index,
                                           self.size_list_1).json_dict)
        for _ in range(self.nb_json):
            index += 1
            new_json = JsonGenerator(f"{self.name}{index}",
                                     self.conf_json.nb_string,
                                     self.conf_json.nb_obj, self.conf_json.size_obj_1,
                                     self.conf_json.nb_json, self.conf_json.conf_json).json_dict

            key = f"{self.name}-{index}"
            value = new_json
            new_dict = {key: value}
            final_json_dict.update(new_dict)

        return final_json_dict

    def json_file(self, path: str):
        with open(path, mode='w', encoding='utf8') as file_handler:
            file_handler.write(json.dumps(self.json_dict))


if __name__ == '__main__':
    # 2 level
    my_json = JsonGenerator(name=1,
                            nb_string=2,
                            nb_obj=2, size_obj_1=3,
                            nb_json=3, conf_json=ConfJson(2, 2, 2))
    my_json.json_file("json_objects_2_levels.json")

    # 3 level
    my_json = JsonGenerator(name=2,
                            nb_string=2,
                            nb_obj=2, size_obj_1=3,
                            nb_json=3, conf_json=ConfJson(2, 2, 2,
                                                          1, ConfJson(1, 2, 2)))
    my_json.json_file("json_objects_3_levels.json")
