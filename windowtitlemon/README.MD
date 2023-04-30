this PoSHscript runs loops to watch a specific window title and updates the name in a file. the fact the files and variables are called "nowplaying" and such may be a pointer to what apps we'Re talking about
# requirements
a windows OS with powershell
# usage
- launch the script with powershell
- you now have a file that you can watch that is being updated with the window title every second
# configuration
edit the file, the first 3 lines define the things
- nowplaying and newplaying are file paths to write to
- appname is the name of the process we're looking at
# shortcomings
- most likely confused when there's multiple processes with the same display name
- it uses 2 different files because at the time of creation, the writer didn't really look too much into learning how to deal with PoSh objects
