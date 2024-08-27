# PaddleOcr转为ONNX

[模型下载](https://paddlepaddle.github.io/PaddleOCR/model/index.html)

# 模型转换

> 注意依赖包paddle2onnx需要python<= 3.9, 代码提供的示例为pp-ocrv4的模型预训练文件, 如果需要转换其他模型,需删除input和output文件夹的所有内容

下载模型后,解压移动到input文件夹

```shell
pip install requirements-dev.lock
python main.py
# or
rye sync
rye run python main.py
```