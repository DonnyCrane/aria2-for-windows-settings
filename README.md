# aria2-for-windows-settings
BT Trackers auto update from login the system

Windows 11 x64环境下，使用python脚本，自动更新BT-Trackers到aria2c.conf。

将HideRun.vbs快捷方式复制到系统启动文件夹后，每次开机都会自动更新trackers，并后台启动aria2c程序。

1. 安装python最新版，并设置环境变量；

2. 更新并设置pip：

    //更新pip
    pip install pip -U
    
    //设置清华大学pip镜像
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

3. 安装依赖或库
    pip install beautifulsoup4 requests html5lib

4. 双击运行HideRun.vbs

The End.
