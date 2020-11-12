## python 开发环境配置

#### 1. 下载 python 安装包

##### 1.1 首先去 Pycharm 官网，https://www.python.org/，下载python安装包，根据自己电脑的操作系统进行选择，对于windows系统步骤如下：选择Downloads，进入Windows版下载最新版本的python，选择相对应的安装包，点击下载

![](https://github.com/qiweiyang123/IMG/raw/main/1.png)

#### 2. 安装 Python

##### 2.1 在 Windows 64 位系统上安装 Python 3.9.0 的步骤如下：

（1）双击下载后得到的安装文件 python-3.9.0-amd64.exe，将显示安装向导对话框，选中“Add Python3.9.0 to PATH”复选框，表示将自动配置环境变量。

（2）单击“Customize installation”按钮，进行自定义安装（自定义安装可以修改安装路径），在弹出的安装选项对话框中采用默认设置。

（3）单击 Next 按钮，将打开高级选项对话框，在该对话框中，设置安装路径为“D:\Python\Python”（读者可自行设置路径），其他采用默认。

（4）单击 Install 按钮，开始安装 Python。

#### 3. 测试 Python 是否安装成功
Python 安装完成后，需要检测 Python 是否成功安装。打开 cmd 命令，启动命令行窗口，在当前的命令提示符后面输入“python”，按下回车键，如果出现如图所示的信息，则说明 Python 安装成功，同时系统进入交互式 Python 解释器中。
  
![](https://github.com/qiweiyang123/IMG/raw/main/2.png)

#### 4. 配置环境变量

先右键 python.exe，选择属性，把路径 Ctrl+C 复制出来。
进入系统属性，找到高级系统设置，点击环境变量，在系统变量中找到 PATH，双击打开，点击新建，然后把刚才复制的 python.exe 的路径复制过去。

![](https://github.com/qiweiyang123/IMG/raw/main/3.png)

![](https://github.com/qiweiyang123/IMG/raw/main/4.png)

![](https://github.com/qiweiyang123/IMG/raw/main/5.png)

然后一直点确定。最后打开 cmd，直接输入 python。

![](https://github.com/qiweiyang123/IMG/raw/main/2.png)
