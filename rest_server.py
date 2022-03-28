"""
Simple rest server to expose your created files
"""
import os

from flask import Flask, json

api = Flask(__name__)


@api.route('/complexity1_k_h_100', methods=['GET'])
def complexity1_k_h_100():

    file_path = 'json_generator/json_generator/complexity1_k_h_100.json'
    with open(file_path) as json_file:
        print(f"REST delivered [{file_path}] with GET")
        return json.loads(json_file.read())


@api.route('/complexity1_k_nh_100', methods=['GET'])
def complexity1_k_nh_100():

    content = [f for f in os.listdir(os.path.join(os.getcwd(), "generation"))]

    print(f"Possibles files:{content}")
    file_path = 'generation/complexity1_k_nh_100.json'

    try:
        with open(file_path) as json_file:
            print(f"REST delivered [{file_path}] with GET")
            return json.loads(json_file.read())
    except FileNotFoundError:
        print(f"REST deliver failed [{file_path}]  not found")
        return "202"


if __name__ == '__main__':
    api.run()
