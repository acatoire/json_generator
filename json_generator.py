"""
Simple json generator with complexity possibilities
"""
from __future__ import annotations
import json
import random
import time


class ConfJson:
    """
    Json Object config
    """

    def __init__(self, nb_string,
                 nb_obj=0, size_obj=0,
                 nb_json=0, conf=None,
                 nb_list: int = 0, conf_lst: ConfJson = None):
        """
        Json Object config
        :param nb_string:
        :param nb_obj:
        :param size_obj:
        :param nb_json:
        :param conf:
        """
        self.nb_string = nb_string
        self.nb_obj = nb_obj
        self.size_obj = 0 if not nb_obj else size_obj
        self.nb_json = nb_json
        self.conf = None if not nb_json else conf
        self.nb_list = nb_list
        self.nb_list_elements = 0 if not nb_list else nb_list_elements
        self.conf_lst = None if not nb_list else conf_lst


class JsonElement:

    @property
    def json_dict(self):
        raise NotImplementedError


class JsonString(JsonElement):

    def __init__(self, prefix: int or str, number: int, index: int, list_index: int = None,
                 kiss=None):
        self.prefix = str(prefix)
        self.number = number
        self.index = index
        self.list_index = list_index
        self.kiss = kiss

    @property
    def json_dict(self):

        if self.kiss is None:
            key = f"{self.prefix}-{self.number}"
        else:
            key = f"-{self.number}"

        if self.kiss is None:
            if self.list_index is None:
                value = f"{self.prefix}{self.number}.{self.index}"
            else:
                value = f"{self.prefix}{self.number}L{self.list_index}.{self.index}"
        else:
            value = self.kiss

        new_dict = {key: value}
        return new_dict


class JsonObj(JsonElement):

    def __init__(self, prefix: int or str, number: int, index: int,
                 nbr_inside_list: int,
                 kiss=None,
                 heterogeneous_schema: bool = True):
        if kiss is None:
            self.prefix = str(prefix)
        else:
            self.prefix = ''

        self.number = number
        self.index = index
        self.nbr_inside_obj = nbr_inside_list
        self.kiss = kiss
        self.heterogeneous_schema = heterogeneous_schema

    @property
    def json_dict(self):

        if self.kiss is None:
            key = f"{self.prefix}-{self.number}"
        else:
            key = f"-{self.number}"

        if self.kiss is None:
            value = JsonGenerator(f"{self.prefix}{self.number}",
                                  ConfJson(self.nbr_inside_obj),
                                  heterogeneous_schema=self.heterogeneous_schema).json_dict
        else:
            value = self.kiss
        new_dict = {key: value}
        return new_dict


class JsonGenerator:

    def __init__(self, name,
                 json_config: ConfJson,
                 list_index: int = None,
                 kiss: str = None,
                 heterogeneous_schema: bool = True):
        self.name = str(name)
        self.json_config = json_config
        self.list_index = list_index
        self.kiss = kiss
        self.heterogeneous_schema = heterogeneous_schema

    @property
    def json_dict(self):
        if self.kiss is None:
            if self.list_index is None:
                id_value = f"{self.name}"
            else:
                id_value = f"{self.name}L{self.list_index}"
        else:
            if self.list_index is None:
                id_value = ""
            else:
                id_value = f"L{self.list_index}"

        final_json_dict = {"id": id_value}
        index = 0

        # Randomize schema if needed
        if self.heterogeneous_schema:
            creation_nb_string = self.json_config.nb_string
            creation_nb_obj = self.json_config.nb_obj
            creation_nb_json = self.json_config.nb_json
            creation_nb_list = self.json_config.nb_list
        else:
            try:
                creation_nb_string = random.randint(1, self.json_config.nb_string)
            except ValueError:
                creation_nb_string = self.json_config.nb_string
            try:
                creation_nb_obj = random.randint(1, self.json_config.nb_obj)
            except ValueError:
                creation_nb_obj = self.json_config.nb_obj
            try:
                creation_nb_json = random.randint(1, self.json_config.nb_json)
            except ValueError:
                creation_nb_json = self.json_config.nb_json
            try:
                creation_nb_list = random.randint(1, self.json_config.nb_list)
            except ValueError:
                creation_nb_list = self.json_config.nb_list

        # Create Strings
        for _ in range(creation_nb_string):
            index += 1
            final_json_dict.update(JsonString(self.name, index, index,
                                              list_index=self.list_index,
                                              kiss=self.kiss).json_dict)

        # Create objects
        for _ in range(creation_nb_obj):
            index += 1
            final_json_dict.update(JsonObj(prefix=self.name, number=index, index=index,
                                           nbr_inside_list=self.json_config.size_obj,
                                           kiss=self.kiss).json_dict)

        # Create complex json
        for _ in range(creation_nb_json):
            index += 1
            new_json = JsonGenerator(
                name=f"{self.name}{index}",
                json_config=self.json_config.conf,
                list_index=self.list_index,
                kiss=self.kiss, heterogeneous_schema=self.heterogeneous_schema).json_dict

            key = f"{self.name}-{index}"
            value = new_json
            new_dict = {key: value}
            final_json_dict.update(new_dict)

        # Create list of complex json
        for _ in range(creation_nb_list):
            index += 1
            list_of_json = []

            # Randomize schema if needed
            if self.heterogeneous_schema:
                creation_nb_elements = self.json_config.nb_list_elements
            else:
                try:
                    creation_nb_elements = random.randint(1, self.json_config.nb_list_elements)
                except ValueError:
                    creation_nb_elements = self.json_config.nb_list_elements

            for list_index in range(creation_nb_elements):
                new_json = JsonGenerator(
                    name=f"{self.name}{index}",
                    json_config=self.json_config.conf_lst,
                    list_index=list_index,
                    kiss=self.kiss, heterogeneous_schema=self.heterogeneous_schema).json_dict

                list_of_json.append(new_json)
            key = f"{self.name}-{index}"
            new_dict = {key: list_of_json}
            final_json_dict.update(new_dict)

        return final_json_dict

    def generate_json_file(self, path: str):

        time_start = time.time()
        with open(path, mode='w', encoding='utf8') as file_handler:
            file_handler.write(json.dumps(self.json_dict))

        time_end = time.time()
        duration = time.strftime('%H:%M:%S', time.gmtime(time_end - time_start))
        print(f"Creation of {path} take {duration}mn")
