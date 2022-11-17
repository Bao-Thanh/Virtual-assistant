from json import loads
import subprocess
from os import startfile

def get_apps():
    cmd = 'powershell -ExecutionPolicy Bypass "Get-StartApps|convertto-json"'
    command = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    command_output = command.stdout.read()
    command_output = command_output.decode('cp850')
    apps=loads(command_output)
    names = {}
    for each in apps:
        names.update({each['Name']:each['AppID']})
    return names
    
def find_app(app_name):
	apps = get_apps()
	for each in sorted(apps,key=len):
		if app_name.upper() in each.upper():
			return each,apps[each]
	else:
		return "Application not found!"

def open_app(app_name):
	app = find_app(app_name)
	if app == None:
		raise ValueError('Application not found!')
	else:
		startfile('shell:AppsFolder\%s'%app[1])

if __name__=='__main__':
        find_app('stealth pc monitor')
