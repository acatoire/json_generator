"""
Simple rest server to expose your created files
"""
import os
from os import listdir
from os.path import isfile, join

OUTPUT_PATH = "tmp/file_list.csv"


def list_files(mypath):

    content = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(f"Possibles files:{content}")

    with open(OUTPUT_PATH, mode='w', encoding='utf8') as result_file:

        result_file.write("file_name, nb_attributes, nb_objects_in_list, deep, schema, "
                          "size(o),  size (ko), size (mo), nb_obj, nb_list")

        for file_name in content:
            if ".json" not in file_name:
                continue
            complete_path = join(mypath, file_name)
            size = os.path.getsize(complete_path)

            info = file_name.replace("A", ";").replace("L", ";").replace("D", ";").replace("_", ";")
            info = info.split(';')
            nb_attributes = info[1]
            nb_objects_in_list = info[2]
            deep = info[3]
            schema = info[4]
            with open(complete_path, mode='r') as json_file:
                file_content = json_file.read()
                nb_obj = file_content.count("id")
                nb_list = file_content.count("[")

            file_stat = (f"{file_name}, {nb_attributes}, {nb_objects_in_list}, {deep}, {schema}, "
                         f"{size}o,  {size/1024:0.1f}ko,   {size/1024/1024:0.1f}mo, {nb_obj}, {nb_list}")

            print(file_stat)
            result_file.write(file_stat + "\n")


if __name__ == '__main__':
    list_files("generation")
