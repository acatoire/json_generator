
"""
Simple json generator with complexity possibilities
"""
import json
import string


class JsonElement:

    @property
    def json_dict(self):
        raise NotImplemented


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
        self.nbr_inside_list = nbr_inside_list

    @property
    def json_dict(self):
        key = f"{self.prefix}-{self.number}"
        value = Json(f"{self.prefix}{self.number}", self.nbr_inside_list).json_dict
        new_dict = {key: value}
        return new_dict


class Json:

    def __init__(self, name,
                 nb_string,
                 nb_obj=0, size_obj_1=0,
                 nb_json=0, conf_json=None):
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
        for i in range(self.nb_string):
            index += 1
            final_json_dict.update(JsonString(self.name, index, index).json_dict)
        for i in range(self.nb_obj):
            index += 1
            final_json_dict.update(JsonObj(self.name, index, index,
                                           self.size_list_1).json_dict)
        for i in range(self.nb_json):
            index += 1
            final_json_dict.update(Json(self.name,
                                        self.conf_json[0], self.conf_json[1],
                                        self.conf_json[2]).json_dict)
        return final_json_dict


if __name__ == '__main__':

    json_dict = Json(1,
                     2,
                     2, 3,
                     1, (1, 2, 2)).json_dict
    print(json.dumps(json_dict))

