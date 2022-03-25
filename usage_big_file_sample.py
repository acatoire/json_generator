
"""
Usage sample of json generator to create massive files
"""

from json_generator import JsonGenerator, ConfJson

if __name__ == '__main__':
    KISS = 'o'
    # Massive
    NB_LIST_LEVEL1 = 100
    NB_STR_IN_LIST_LEVEL1 = 10
    NB_LIST_LEVEL2 = 100
    NB_STR_IN_LIST_LEVEL2 = 10
    NB_LIST_LEVEL3 = 100
    NB_STR_IN_LIST_LEVEL3 = 10

    my_json = JsonGenerator(
        name=5,
        json_config=ConfJson(nb_string=0,
                             nb_list=1, nb_list_elements=NB_LIST_LEVEL1,
                             conf_lst=ConfJson(nb_string=NB_STR_IN_LIST_LEVEL1,
                                               nb_list=1, nb_list_elements=NB_LIST_LEVEL2,
                                               conf_lst=ConfJson(nb_string=NB_STR_IN_LIST_LEVEL2,
                                                                 nb_list=1,
                                                                 nb_list_elements=NB_LIST_LEVEL3,
                                                                 conf_lst=ConfJson(nb_string=NB_STR_IN_LIST_LEVEL3)
                                                                 )
                                               )
                             ),
        kiss=KISS)

    my_json.generate_json_file("generation/json_massive.json")

    my_json = JsonGenerator(
        name=5,
        json_config=ConfJson(nb_string=0,
                             nb_list=1, nb_list_elements=NB_LIST_LEVEL1,
                             conf_lst=ConfJson(nb_string=NB_STR_IN_LIST_LEVEL1,
                                               nb_list=1, nb_list_elements=NB_LIST_LEVEL2,
                                               conf_lst=ConfJson(nb_string=NB_STR_IN_LIST_LEVEL2,
                                                                 nb_list=1,
                                                                 nb_list_elements=NB_LIST_LEVEL3,
                                                                 conf_lst=ConfJson(nb_string=NB_STR_IN_LIST_LEVEL3)
                                                                 )
                                               )
                             ),
        kiss=None)

    my_json.generate_json_file("generation/json_massive_nokiss.json")
