#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import pathlib


def tree(directory: pathlib.Path, max_depth: int = None, level: int = 0):
    # Проверка: является ли переданный объект пути директорией,
    # если нет, то возвращается None
    if not directory.is_dir():
        return

    # Проверка: превышает ли текущий уровень заданную глубину,
    # если нет, то возвращается None
    if max_depth is not None and level >= max_depth:
        return

    # Перебираем все элементы директории
    for item in directory.iterdir():
        print("  " * level + "- " + item.name)
        # Если элемент является директорией, то вызывается рекурсивно
        # функция tree() с уровнем на 1 больше
        if item.is_dir():
            tree(item, max_depth, level + 1)


if __name__ == "__main__":
    # description="Выводит структуру директорий"
    parser = argparse.ArgumentParser(add_help=False)

    # Добавление аргумента для пути к каталогу, который не является обязательным
    # Если он не указан, то выводится текущий рабочий каталог
    parser.add_argument("directory", type=pathlib.Path, default=pathlib.Path.cwd(),
                        nargs="?", help="Каталог для отображения (по умолчанию: текущий каталог)")

    # Добавление аргумента для максимальной глубины рекурсивного обхода каталога
    parser.add_argument("-d", "--depth", type=int, default=None,
                        help="Максимальная глубина каталогов")
    args = parser.parse_args()

    tree(args.directory, args.depth)
