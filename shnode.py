#!/usr/bin/python

# shNode Smart Home Node Applicationt
# Joshua Besneatte http://github.com/shamanon/shNode

# This program performs the following actions:
# Parse all module data in XML or List format
# Write Module data to log
# Read Log to stdout

# To Do
# Send commands to extensions

import jxmlease, glob, subprocess, sys, time

mod_folder = '/opt/shNode'

# run modules - default
def dataView(mod_folder):
	folders = glob.glob(mod_folder+'/modules/shNode.*')
	output = str()
	for i in folders:
		proc = subprocess.Popen(i+'/status', stdout=subprocess.PIPE)
		output = output+str(proc.stdout.read())
	print str.strip(output)

# collect and concatinate data
def dataXML(mod_folder):
	folders = glob.glob(mod_folder+'/modules/shNode.*')
	data = '{\'shNode\': {'
	for i in folders:
		proc = subprocess.Popen(i+'/data', stdout=subprocess.PIPE)
		output = proc.stdout.read()
		data = data+str(jxmlease.parse(output))
	data = data+'}'
	data = data.replace('{{','{')
	data = data.replace('}}{', '}, ')
	print(jxmlease.emit_xml(eval(data)))

# write data to log
def dataLog():
	folders = glob.glob(mod_folder+'/modules/shNode.*')
	output = str()
	ts = time.time()
	for i in folders:
		proc = subprocess.Popen(i+'/status', stdout=subprocess.PIPE)
		output = output+str(proc.stdout.read())
	log = open(mod_folder+'/log/shnode.log','a')
	log.write('['+str(ts)+'] '+str.strip(output).replace('\n',',').replace(': ',':')+'\n')
	
# display log
def logView():
	subprocess.call(['cat', mod_folder+'/log/shnode.log'])
	print

# do the business
# available command line options
args = { '-x': 'Output XML', '-r': 'Output List', '-l': 'Display Log', '-s': 'Log Data' }

# run the functions according to options
if len(sys.argv) == 2 and sys.argv[1] in args:
	action = args[sys.argv[1]]
	if sys.argv[1] == '-x':
		dataXML(mod_folder)
	elif sys.argv[1] == '-s':
		dataLog()
	elif sys.argv[1] == '-l':
		logView()
	else:
		dataView(mod_folder)
else:
    print('Usage: shnode <option>')
    print('Options: \n  '+str(args).replace('{', '').replace('}', '').replace('\'', '').replace(', ', '\n  '))
    sys.exit(1)
