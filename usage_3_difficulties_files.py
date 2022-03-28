"""
Usage sample of json generator to create massive files
"""

from json_generator import JsonGenerator, ConfJson

NB_IN_LIST_1 = 500
NB_IN_LIST_2 = 10000
NB_IN_LIST_3 = 100000

# Complexity 1
C1_NB_ATTRIBUTES = 8
C1_NB_OBJ = 2
C1_NB_OBJ_ATTRIBUTES = 10
C1_NB_SUB_OBJ = 0
C1_NB_SUB_OBJ_ATTRIBUTES = 0

# Complexity 2
C2_NB_ATTRIBUTES = 5
C2_NB_OBJ = 5
C2_NB_OBJ_ATTRIBUTES = 7
C2_NB_SUB_OBJ = 3
C2_NB_SUB_OBJ_ATTRIBUTES = 5

# Complexity 3
C3_NB_ATTRIBUTES = 20
C3_NB_OBJ = 30
C3_NB_OBJ_ATTRIBUTES = 10
C3_NB_SUB_OBJ = 20
C3_NB_SUB_OBJ_ATTRIBUTES = 5


def make_json(complexity_id,
              kiss: str = None, heterogeneous: bool = True,
              nb_in_list: int = 5,
              nb_attributes: int = 10, nb_obj: int = 0,
              nb_obj_attributes: int = 0, nb_sub_obj: int = 0,
              nb_sub_obj_attributes: int = 0):
    """
    Create a json depending on the parameters:
    :param complexity_id:
    :param kiss:
    :param heterogeneous:
    :param nb_in_list:
    :param nb_attributes:
    :param nb_obj:
    :param nb_obj_attributes:
    :param nb_sub_obj:
    :param nb_sub_obj_attributes:
    :return:

    The Json structure will be as follow:

    {
    "id": "xxxxx",
    "array-1": [
      {},              # nb_in_list elements in the array
      [...]            # nb_in_list elements in the array
      {                # nb_in_list elements in the array
        "id": "L0",
        "-1": "o",        # nb_attributes
        [...]             # nb_attributes
        "-7": "o",        # nb_attributes
        "C3L1001-8": {} , # nb_obj
        [...]             # nb_obj
        "C3L1001-xx": {   # nb_obj
        {
          "id": "L0",
          "-1": "o",              # nb_obj_attributes
          [...]                   # nb_obj_attributes
          "-9": "o",              # nb_obj_attributes
          "C3L1001xx-10": {},     # nb_sub_obj
          [...]                   # nb_sub_obj
          "C3L1001xx-yy": {       # nb_sub_obj
            "id": "L0",
            "-1": "o"                # nb_sub_obj_attributes
            [...]                    # nb_sub_obj_attributes
            "-x": "o"                # nb_sub_obj_attributes
            }
        },
    }


    """
    kiss_str = "_k" if kiss else ""
    heterogeneous_str = "_h" if heterogeneous else "_nh"

    my_json = JsonGenerator(
        name=f"C{complexity_id}L{nb_in_list}",
        json_config=ConfJson(
            nb_string=0,
            nb_list=1, nb_list_elements=nb_in_list, conf_lst=ConfJson(
                nb_string=nb_attributes,
                nb_json=nb_obj, conf=ConfJson(
                    nb_string=nb_obj_attributes,
                    nb_json=nb_sub_obj, conf=ConfJson(nb_string=nb_sub_obj_attributes)))
        ),
        kiss=kiss, heterogeneous_schema=heterogeneous)

    my_json.generate_json_file(f"generation/complexity{complexity_id}{kiss_str}{heterogeneous_str}_{nb_in_list}.json")


def make_3_complexity_files(nb_in_list: int, heterogeneous: bool = True,):
    # Heterogeneous
    make_json(
        complexity_id=1,
        kiss='o', heterogeneous=heterogeneous,
        nb_in_list=nb_in_list,
        nb_attributes=C1_NB_ATTRIBUTES, nb_obj=C1_NB_OBJ,
        nb_obj_attributes=C1_NB_OBJ_ATTRIBUTES, nb_sub_obj=C1_NB_SUB_OBJ,
        nb_sub_obj_attributes=C1_NB_SUB_OBJ_ATTRIBUTES
    )
    make_json(
        complexity_id=2,
        kiss='o', heterogeneous=heterogeneous,
        nb_in_list=nb_in_list,
        nb_attributes=C2_NB_ATTRIBUTES, nb_obj=C2_NB_OBJ,
        nb_obj_attributes=C2_NB_OBJ_ATTRIBUTES, nb_sub_obj=C2_NB_SUB_OBJ,
        nb_sub_obj_attributes=C2_NB_SUB_OBJ_ATTRIBUTES
    )
    make_json(
        complexity_id=3,
        kiss='o', heterogeneous=heterogeneous,
        nb_in_list=nb_in_list,
        nb_attributes=C3_NB_ATTRIBUTES, nb_obj=C3_NB_OBJ,
        nb_obj_attributes=C3_NB_OBJ_ATTRIBUTES, nb_sub_obj=C3_NB_SUB_OBJ,
        nb_sub_obj_attributes=C3_NB_SUB_OBJ_ATTRIBUTES
    )


if __name__ == '__main__':

   # Non Heterogeneous
   make_3_complexity_files(NB_IN_LIST_1, True)
   make_3_complexity_files(NB_IN_LIST_2, True)
   make_3_complexity_files(NB_IN_LIST_3, True)
   # Non Heterogeneous
   make_3_complexity_files(NB_IN_LIST_1, False)
   make_3_complexity_files(NB_IN_LIST_2, False)
   make_3_complexity_files(NB_IN_LIST_3, False)
