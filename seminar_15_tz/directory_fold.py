from collections import namedtuple
import os
from seminar_15_tz.log_utilit import common_log

FObject = namedtuple('FObject', 'dir_parent',
                     defaults=['', '', False, ''])  # (имя файла, расширение, директория или нет,


# родительская директория) - кортеж
def dir_page(path_string: str):
    f_objects = []
    if not path_string:
        path_string = os.getcwd()
        common_log.warning(f'Путь установлен по умолчанию {path_string}')
    path_string = os.path.abspath(path_string)
    parent = path_string.rstrip('/').rsplit('/', 1)[1]  # получаем абсолютный путь
    try:
        for item in os.listdir(path_string):
            obj_name, obj_ext = None, None
            item: str = item.rsplit('/', 1)[1]
            if item.rfind('.') != -1 and not item.startswith('.'):
                obj_name, obj_ext = item.rsplit('.', 1)
            else:
                obj_name = item
            f_objects.append(FObject(name=obj_name, ext=obj_ext, parent=parent, is_dir=False))
        common_log.info(msg=str(f_objects[-1]))
    except Exception as exc:
        print(f'\033[31mERRORR: {exc.__class__.name__}: {exc}\033[0m')
        common_log.error(msg=f'{exc.__class__.name__}: {exc}')
    return f_objects  # список наименованных кортежей


if __name__ == '__main__':
    print('Not for separate use')
