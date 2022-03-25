
"""
Simple usage sample of json generator
"""

from json_generator import JsonGenerator, ConfJson

if __name__ == '__main__':
    KISS = None
    # KISS = 'o'

    # 1 level
    my_json = JsonGenerator(name=1,
                            json_config=ConfJson(nb_string=0,
                                                 nb_json=2, conf=ConfJson(3)),
                            kiss=KISS)
    my_json.generate_json_file("generation/json_objects_1_levels.json")

    # 2 level
    my_json = JsonGenerator(name=1,
                            json_config=ConfJson(nb_string=2,
                                                 nb_obj=2, size_obj=3,
                                                 nb_json=3, conf=ConfJson(2, 2, 2)),
                            kiss=KISS)
    my_json.generate_json_file("generation/json_objects_2_levels.json")

    # 3 level
    my_json = JsonGenerator(name=2,
                            json_config=ConfJson(nb_string=2,
                                                 nb_obj=2, size_obj=3,
                                                 nb_json=3, conf=ConfJson(2, 2, 2,
                                                                          1, ConfJson(1, 2, 2))),
                            kiss=KISS)
    my_json.generate_json_file("generation/json_objects_3_levels.json")

    # only one list
    my_json = JsonGenerator(name=2,
                            json_config=ConfJson(nb_string=2,
                                                 nb_obj=3, size_obj=3,
                                                 nb_json=4, conf=ConfJson(2, 2, 2),
                                                 nb_list=1, nb_list_elements=5, conf_lst=ConfJson(nb_string=2)),
                            kiss=KISS)
    my_json.generate_json_file("generation/json_only_one_list.json")

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
                            kiss=KISS)

    my_json.generate_json_file("generation/json_2_level_list.json")

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
                            kiss=KISS)

    my_json.generate_json_file("generation/json_3_level_list.json")
