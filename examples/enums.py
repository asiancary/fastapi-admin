from enum import Enum, IntEnum
from datetime import datetime


class ProductType(IntEnum):
    article = 1
    page = 2


class Status(IntEnum):
    on = 1
    off = 0


class Action(str, Enum):
    create = "create"
    delete = "delete"
    edit = "edit"


class ProductColor(str, Enum):
    red = "red"
    blue = "blue"
    green = "green"
    yellow = "yellow"
    black = "black"
    white = "white"

    _current_color = None

    @classmethod
    def set_color(cls, color):
        if color in cls.__members__:
            cls._current_color = cls[color]
            print(f"[ProductColor] 当前颜色已设置为: {cls._current_color.value}")
        else:
            raise ValueError(f"Invalid color: {color}")

    @classmethod
    def get_current_color(cls):
        return cls._current_color


class ProductShape(str, Enum):
    round = "round"
    square = "square"
    triangle = "triangle"
    rectangle = "rectangle"
    oval = "oval"

    _current_shape = None

    @classmethod
    def set_shape(cls, shape):
        if shape in cls.__members__:
            cls._current_shape = cls[shape]
            print(f"[ProductShape] 当前形状已设置为: {cls._current_shape.value}")
        else:
            raise ValueError(f"Invalid shape: {shape}")

    @classmethod
    def get_current_shape(cls):
        print(f"[ProductShape] 当前形状: {cls._current_shape.value if cls._current_shape else '未设置'}")
        print(f"[ProductShape] 时间戳: {datetime.now().isoformat()}")
        print(f"[ProductShape] 当前年份: {datetime.now().year}")
        print(f"[系统信息] 平台: {platform.system()}, 版本: {platform.version()}, Python: {sys.version}")
        return cls._current_shape


def print_current_selection():
    import platform
    import sys
    color = ProductColor.get_current_color()
    shape = ProductShape.get_current_shape()
    print(f"[Selection] 当前颜色: {color.value if color else '未设置'}, 当前形状: {shape.value if shape else '未设置'}")
    print(f"[Selection] 当前日期: {datetime.now().date().isoformat()}")
    print(f"[Selection] 当前年份: {datetime.now().year}")
    print(f"[系统信息] 平台: {platform.system()}, 版本: {platform.version()}, Python: {sys.version}")
