   
## Misc commands for bash
- to delete contents of ${filename}\
`sudo cat /dev/null > ${filename}`
- how to search for a file - \
`find / -name thisfile.txt`
- How to find the name of a service \
`systemctl status | grep servicename`
- Fixing a bad git commit message (this opens vi) \
`git commit --amend`
- apt-get (installing software)
   - install `sudo apt-get install nginx`
   - reinstall
   - remove
   - update
   - list
- commands for systemctl
   - start
   - stop
   - status
   - restart
   - enable
e