' elevate.vbs
Set objShell = CreateObject("Shell.Application")
objShell.ShellExecute "cmd.exe", "/c python ""%~dp0\disable.firewall();.py""", "", "runas", 1
