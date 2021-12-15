# aria2-for-windows-settings

Windows 11 x64环境下，使用python脚本，自动更新BT-Trackers到aria2c.conf。<br>

将HideRun.vbs快捷方式复制到系统启动文件夹后，每次开机都会自动更新trackers，并后台启动aria2c程序。<br>

1. 安装python最新版，并设置环境变量；

2. 更新并设置pip：<br>
    //更新pip<br>
    pip install pip -U<br>
    //安装依赖或库<br>
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple<br>

3. 安装依赖或库<br>
    pip install beautifulsoup4 requests html5lib<br>
    
4. 双击运行HideRun.vbs<br>

The End.<br>
