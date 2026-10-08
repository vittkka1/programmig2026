def get_file_type(extension):
    file_type={".jpg":"Зображення", ".mp3":"Аудіо", ".py":"Скрипт Python"}
    return file_type.get(extension,"Невідомий формат")
