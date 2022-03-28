
"""
Simple usage sample of json generator
"""

from json_generator import JsonGenerator, ConfJson


def method_name(kiss: str = None, homogeneous: bool = True):

    kiss_str = "_kiss" if kiss else ""
    homogeneous_str = "_homogeneous" if homogeneous else "_non_homogeneous"

    # 1 level
    my_json = JsonGenerator(name=1,
                            json_config=ConfJson(nb_string=0,
                                                 nb_json=2, conf=ConfJson(3)),
                            kiss=kiss, homogeneous_schema=homogeneous)
    my_json.generate_json_file(f"generation/json_1_levels{kiss_str}{homogeneous_str}.json")
    # 2 level
    my_json = JsonGenerator(name=1,
                            json_config=ConfJson(nb_string=2,
                                                 nb_obj=2, size_obj=3,
                                                 nb_json=3, conf=ConfJson(2, 2, 2)),
                            kiss=kiss, homogeneous_schema=homogeneous)
    my_json.generate_json_file(f"generation/json_2_levels{kiss_str}{homogeneous_str}.json")
    # 3 level
    my_json = JsonGenerator(name=2,
                            json_config=ConfJson(nb_string=2,
                                                 nb_obj=2, size_obj=3,
                                                 nb_json=3, conf=ConfJson(2, 2, 2,
                                                                          1, ConfJson(1, 2, 2))),
                            kiss=kiss, homogeneous_schema=homogeneous)
    my_json.generate_json_file(f"generation/json_3_levels{kiss_str}{homogeneous_str}.json")
    # only one list
    my_json = JsonGenerator(name=2,
                            json_config=ConfJson(nb_string=0,
                                                 nb_obj=0, size_obj=3,
                                                 nb_json=0, conf=ConfJson(2, 2, 2),
                                                 nb_list=1, nb_list_elements=5, conf_lst=ConfJson(nb_string=20)),
                            kiss=kiss, homogeneous_schema=homogeneous)
    my_json.generate_json_file(f"generation/json_one_list{kiss_str}{homogeneous_str}.json")
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
                            kiss=kiss, homogeneous_schema=homogeneous)
    my_json.generate_json_file(f"generation/json_2_level_list{kiss_str}{homogeneous_str}.json")
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
                            kiss=kiss, homogeneous_schema=homogeneous)
    my_json.generate_json_file(f"generation/json_3_level_list{kiss_str}{homogeneous_str}.json")


if __name__ == '__main__':

    method_name(kiss=None, homogeneous=True)
    method_name(kiss='o', homogeneous=True)
    method_name(kiss='o', homogeneous=False)
    method_name(kiss=None, homogeneous=False)
