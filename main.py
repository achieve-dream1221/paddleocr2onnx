#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 16:50
# @Author  : ACHIEVE_DREAM
# @File    : main.py
# @Software: Pycharm

import paddle2onnx
from pathlib import Path


def main():
    input_dir = Path("input")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    if not input_dir.exists():
        raise FileNotFoundError(f"{input_dir} not exists")
    for i in input_dir.iterdir():
        if i.is_file():
            continue
        name = i.name
        paddle2onnx.export(
            model_file=str(i / "inference.pdmodel"),
            params_file=str(i / "inference.pdiparams"),
            opset_version=16,
            save_file=f"{output_dir / name}.onnx",
        )


if __name__ == "__main__":
    main()
