"""
Simple rest server to expose your created files
"""
import os

from flask import Flask, json

api = Flask(__name__)


@api.route('/complexity1', methods=['GET'])
def complexity1():

    file_path = 'generation/deep-A4L4D3_k_h.json'
    return get_from_file(file_path)


@api.route('/complexity1n', methods=['GET'])
def complexity1n():

    file_path = 'generation/deep-A4L4D3_k_nh.json'
    return get_from_file(file_path)


def get_from_file(file_path):

    try:
        with open(file_path) as json_file:
            print(f"REST delivered [{file_path}] with GET")
            return json.loads(json_file.read())
    except FileNotFoundError:
        content = [f for f in os.listdir(os.path.join(os.getcwd(), "generation"))]
        print(f"Possibles files:{content}")
        print(f"REST deliver failed [{file_path}]  not found")
        return "400"


if __name__ == '__main__':
    api.run()
