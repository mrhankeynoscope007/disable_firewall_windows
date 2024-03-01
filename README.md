# disable_firewall_windows
disable_firewall_windows


Purpose: The repository contains scripts to disable the Windows firewall programmatically.

Scripts:

disable_firewall.py: Python script that disables the Windows firewall.
elevate.vbs: VBScript to request administrative privileges and execute the Python script.
disable_firewall.bat: Batch script to execute the VBScript.
disable_firewall.ps1: PowerShell script to request administrative privileges and execute the Python script.
Usage:

Run run_disable_firewall.bat to disable the firewall.
This batch script executes the VBScript, which requests administrative privileges and runs the Python script to disable the firewall.
Execution Flow:

The batch script requests administrative privileges using the VBScript (elevate.vbs).
The VBScript executes the Python script (disable_firewall.py), which disables the Windows firewall.
Note:

Ensure all scripts are placed in the appropriate directories as mentioned in the repository structure for the batch script to work correctly.
Running the provided batch script will handle the process of disabling the firewall, making it a convenient and automated solution.



Python3.11.5
