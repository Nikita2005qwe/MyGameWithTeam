import json

def write_file(data, file_name):
    """Запись файла"""
    data = json.dumps(data)
    data = json.loads(str(data))

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def read_inf(file_name):
    """Чтение файла"""
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)
