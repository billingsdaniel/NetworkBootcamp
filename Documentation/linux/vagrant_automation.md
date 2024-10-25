For automating basic networking, dhcp, dns, and web hosting.
edit vagrantfile
can use external files of shell commands

Example
```Vagrantfile
Vagrant.configure("2") do |config|
  # Configuration for "VB_Router"
  config.vm.define "VB_Router" do |vm1|
    vm1.vm.box = "gusztavvargadr/ubuntu-desktop"
#   Default network card(Eth 0) is usually set to "public_network", type: "dhcp"
#   Adds 2nd network card with the following paramiters
    vm1.vm.network "private_network", ip: "192.168.1.1", virtualbox__intnet: true
    vm1.vm.provider "virtualbox" do |vb1|
      vb1.memory = "3072"
    end
# Provision runs the shell command either specified or links to another file in the same folder at directed path
# In this case, runs the shell commands at first "router_command_lines.sh" and then "dns_command_lines.sh" in order
    vm1.vm.provision "shell", path: "router_command_lines.sh"
    vm1.vm.provision "shell", path: "dns_command_lines.sh"
  end
```
This is a script, so use a shebang to tell the executor that the rest of the file is a bash script\
```#!/bin/bash```

#### -e generates exceptions when getting errors
####  -x prints the command before running, useful for being able to tell where your code is getting hung on when troubleshooting
```set -ex```

#### Using Heredoc 
- Cat prints to command line, and EOF takes that printed data and edits the file at filepath to the new data
- You can use any word to represent the heredoc, and may be useful for reference, but as long as the word between the << and the > are consistent it always works.
- If some characters in your document have other functions, you can put the HEREDOC in quotes `"HEREDOC"` to have the code printed exactly, without calling other functions, You can also use a backslash `\ ` before the special character to do the same, but only for that character. such as `\$TTL` 
```Shell
cat <<HEREDOC > /file/path/here
Text Line 1
Text Line 2
Text Line 3
Text Line 4
HEREDOC
```

#### GUI and Required Inputs
- When automating a vagrant file, some installations (such as apt-get install) require an input to start. you can append the command with `-y` to automatically select yes( more specifically, when the expected input is the letter y)
```
apt-get install iptables-persistent -y
```
- Some installations use GUI, and this can be circumvented with `DEBIAN_FRONTEND=noninteractive`
```
sudo DEBIAN_FRONTEND=noninteractive apt-get install iptables-persistent -y
```

#### Search and Replace File contents from command line
- Uses the `sed` command, greps the correct place to replace, and then replaces only the specified line(s)
```shell
file="/etc/sysctl.conf"
line_to_add="net.ipv4.ip_forward = 1"
# Check if the line exists (but not necessarily with the correct value)
if grep -q "^net.ipv4.ip_forward" "$file"; then
    # If the line exists, update it to ensure it is set to 1
    sudo sed -i 's/^net\.ipv4\.ip_forward.*/net.ipv4.ip_forward = 1/' "$file"
    echo "Line updated in the file."
else
    echo "$line_to_add" | sudo tee -a "$file"
    echo "Line added to the file."
```
