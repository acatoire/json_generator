"""
Usage sample of json generator to create massive files
"""

from json_generator import ConfDeepJson, JsonDeepGenerator

# Complexity 1
C1_NB_ATTRIBUTES = 4
C1_NB_LIST_ELEMENTS = 4
C1_DEEP = 12

# Complexity 2
C2_NB_ATTRIBUTES = 4
C2_NB_LIST_ELEMENTS = 4
C2_DEEP = 13

# Complexity 3
C3_NB_ATTRIBUTES = 4
C3_NB_LIST_ELEMENTS = 4
C3_DEEP = 14


def make_json(kiss: str = None, heterogeneous: bool = True,
              nb_list_elements: int = 5,
              nb_attributes: int = 10, deep: int = 0):
    """
    Create a json depending on the parameters:
    :param kiss:
    :param heterogeneous:
    :param nb_list_elements:
    :param nb_attributes:
    :param deep:
    :return:

    The Json structure will be as follow:

    {
        "id": "1"
        "att_1-1": "val_1-1",       # nb_attributes
        "att_1-2": "val_1-2",       # nb_attributes
        "array": [
           {                            # nb_list_elements
            "id": "1*1"
            "att_1*1-1": "val_1",              # nb_attributes
            "att_1*1-2": "val_2",              # nb_attributes
            "array": [
                {.....},                            # nb_list_elements
                {.....},                            # nb_list_elements
                {.....},                            # nb_list_elements
            ]
           },
           {.....},                     # nb_list_elements
           {.....},                     # nb_list_elements
        ]
    }


    """
    kiss_str = "_k" if kiss else ""
    heterogeneous_str = "_h" if heterogeneous else "_nh"

    my_json = JsonDeepGenerator(
        name=f"A{nb_attributes}L{nb_list_elements}D{deep}",
        config=ConfDeepJson(nb_string=nb_attributes,
                            nb_list=1, nb_list_elements=nb_list_elements),
        deep=deep,
        kiss=kiss, heterogeneous_schema=heterogeneous)

    my_json.generate_json_file(
        f"generation/deep-A{nb_attributes}L{nb_list_elements}D{deep}{kiss_str}{heterogeneous_str}.json")


def make_3_complexity_files(heterogeneous: bool = True):

    make_json(
        kiss='o', heterogeneous=heterogeneous,
        nb_attributes=C1_NB_ATTRIBUTES,
        nb_list_elements=C1_NB_LIST_ELEMENTS,
        deep=C1_DEEP
    )
    make_json(
        kiss='o', heterogeneous=heterogeneous,
        nb_attributes=C2_NB_ATTRIBUTES,
        nb_list_elements=C2_NB_LIST_ELEMENTS,
        deep=C2_DEEP
    )
    make_json(
        kiss='o', heterogeneous=heterogeneous,
        nb_attributes=C3_NB_ATTRIBUTES,
        nb_list_elements=C3_NB_LIST_ELEMENTS,
        deep=C3_DEEP
    )


if __name__ == '__main__':

    # Non Heterogeneous
    make_3_complexity_files(True)
    # Non Heterogeneous
    make_3_complexity_files(False)