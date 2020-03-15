# shNode
Smart Home Node Module Reader and Data Serving Service 

Any hardware that can be run with the RPi probably already has a snipit of code
on the web somewhere to get the job done. shNode allows you to simply create 
modules (shModules) with these snippits and then make them avialable on the 
local network. Any program in any language can be a shModule as long as it 
outputs and recieves data in proper XML format

How it works: 

The shNode service makes a port available on the device.
Reading this port will output XML formatted data from all shModules installed
on the device. This data can then be parsed by sHome or other XML parser.
