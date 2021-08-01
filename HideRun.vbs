CreateObject("WScript.Shell").Run "python UpdateTrackers.py",0
wscript.sleep 3000
CreateObject("WScript.Shell").Run "aria2c.exe --conf-path=aria2.conf",0