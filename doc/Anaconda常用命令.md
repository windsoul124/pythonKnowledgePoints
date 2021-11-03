Anaconda常用命令

- `conda list`查看安装的所有包

- `conda env list`查看当前存在哪些虚拟环境

- `conda update conda`检查更新当前`conda`

- `conda create -n your_env_name python=X.X`

  `your_env_name`为虚拟环境别名

  `X.X`为创建的`python`版本

- `conda activate your_env_name`激活指定虚拟环境
- `conda install -n your_env_name [package]`对环境安装指定的包
- `conda deactivate`关闭当前虚拟环境并返回默认环境
- `conda remove -n your_env_name -all`删除虚拟环境