
"""
Simple usage sample of json generator
"""

from json_generator import JsonGenerator, ConfJson


def method_name(kiss: str = None, heterogeneous: bool = True):

    kiss_str = "_kiss" if kiss else ""
    heterogeneous_str = "_heterogeneous" if heterogeneous else "_non_heterogeneous"

    # 1 level
    my_json = JsonGenerator(name=1,
                            json_config=ConfJson(nb_string=0,
                                                 nb_json=2, conf=ConfJson(3)),
                            kiss=kiss, heterogeneous_schema=heterogeneous)
    my_json.generate_json_file(f"generation/json_1_levels{kiss_str}{heterogeneous_str}.json")
    # 2 level
    my_json = JsonGenerator(name=1,
                            json_config=ConfJson(nb_string=2,
                                                 nb_obj=2, size_obj=3,
                                                 nb_json=3, conf=ConfJson(2, 2, 2)),
                            kiss=kiss, heterogeneous_schema=heterogeneous)
    my_json.generate_json_file(f"generation/json_2_levels{kiss_str}{heterogeneous_str}.json")
    # 3 level
    my_json = JsonGenerator(name=2,
                            json_config=ConfJson(nb_string=2,
                                                 nb_obj=2, size_obj=3,
                                                 nb_json=3, conf=ConfJson(2, 2, 2,
                                                                          1, ConfJson(1, 2, 2))),
                            kiss=kiss, heterogeneous_schema=heterogeneous)
    my_json.generate_json_file(f"generation/json_3_levels{kiss_str}{heterogeneous_str}.json")
    # only one list
    my_json = JsonGenerator(name=2,
                            json_config=ConfJson(nb_string=0,
                                                 nb_obj=0, size_obj=3,
                                                 nb_json=0, conf=ConfJson(2, 2, 2),
                                                 nb_list=1, nb_list_elements=5, conf_lst=ConfJson(nb_string=20)),
                            kiss=kiss, heterogeneous_schema=heterogeneous)
    my_json.generate_json_file(f"generation/json_one_list{kiss_str}{heterogeneous_str}.json")
    # 2_level_list
    my_json = JsonGenerator(name=5,
                            json_config=ConfJson(nb_string=0,
                                                 nb_obj=0, size_obj=3,
                                                 nb_json=0, conf=ConfJson(nb_string=2, nb_obj=2, size_obj=3),
                                                 nb_list=1, nb_list_elements=2,
                                                 conf_lst=ConfJson(nb_string=0,
                                                                   nb_obj=0, size_obj=1,
                                                                   nb_json=0, conf=ConfJson(nb_string=1),
                                                                   nb_list=1, nb_list_elements=5,
                                                                   conf_lst=ConfJson(nb_string=3))),
                            kiss=kiss, heterogeneous_schema=heterogeneous)
    my_json.generate_json_file(f"generation/json_2_level_list{kiss_str}{heterogeneous_str}.json")
    # 3_level_list
    my_json = JsonGenerator(name=5,
                            json_config=ConfJson(nb_string=0,
                                                 nb_obj=0, size_obj=3,
                                                 nb_json=0, conf=ConfJson(nb_string=2, nb_obj=2, size_obj=3),
                                                 nb_list=1, nb_list_elements=3,
                                                 conf_lst=ConfJson(nb_string=0,
                                                                   nb_obj=0, size_obj=1,
                                                                   nb_json=0, conf=ConfJson(nb_string=1),
                                                                   nb_list=1, nb_list_elements=2,
                                                                   conf_lst=ConfJson(nb_string=0,
                                                                                     nb_obj=0, size_obj=1,
                                                                                     nb_json=0,
                                                                                     conf=ConfJson(nb_string=1),
                                                                                     nb_list=1, nb_list_elements=5,
                                                                                     conf_lst=ConfJson(nb_string=3)))),
                            kiss=kiss, heterogeneous_schema=heterogeneous)
    my_json.generate_json_file(f"generation/json_3_level_list{kiss_str}{heterogeneous_str}.json")


if __name__ == '__main__':

    method_name(kiss=None, heterogeneous=True)
    method_name(kiss='o', heterogeneous=True)
    method_name(kiss='o', heterogeneous=False)
    method_name(kiss=None, heterogeneous=False)
