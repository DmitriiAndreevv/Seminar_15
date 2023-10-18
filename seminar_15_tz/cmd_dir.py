# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# - имя файла без расширения или название каталога,
# - расширение, если это файл,
# - флаг каталога,
# - название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import argparse
from seminar_15_tz.directory_fold import dir_page


def parse_ars():
    parse = argparse.ArgumentParser(description="hw15_task_1")
    parse.add_argument('-p', metavar='path', type=str, nargs='-', default='.', help='Введите путь директории')
    args = parse.parse_args()
    return args.p


def main():
    for place in parse_ars():
        for item in (dir_page(place)):
            print(repr(item))


if __name__ == '__main__':
    main()

# .\seminar_15_tz\cmd_dir.py -p hw15_utilits ..\task1  - запуск из командной строки
