# back-end-python-server
## 文件介绍
- venv是一个python的虚拟环境
- dysms_python 是aliyun的接口文件

## <font color=red>注意事项</font>
1. 修改dysms_python文件夹中的const_example.py文件参数，并改名为const.py
2. 修改配置文件config_example.py，并改名为config.py
3. 完成上述步骤才可以执行python_backend_api.py

## 执行步骤
1. 
```bash
$ git clone https://github.com/NJU-itxia/back-end-python-server.git
```
2. 
```bash
$ cd dysms_python
```
3. 
```bash
$ python setup.py install
```
4. 
```bash
$ vim const_example.py #注意修改参数
$ rename const_example.py const.py const_example.py
$ cd ..
$ vim config_example.py #注意修改参数
$ rename config_example.py config.py config_example.py
```
5. 
```bash
$ python python_backend_api.py
```
