# Hypervisors

## Contents
1. Virtual Box
2. 

## Virtual Box
Installed virtualbox from this link
https://www.virtualbox.org/wiki/Downloads

### Running vagrant vbox in linux
1. `mkdir vagrant_test`
2. `cd vagrant_test`
3. `vagrant init "gusztavvargadr/ubuntu-desktop"`
4. `vagrant up`

### Windows vbox
- StefanScherer/windows_2019 --box-version 2021.05.15

### Troubleshooting
1. Mac address on each new box are identical, needed to randomize them when attempting to practice networking.
2. Vbox defaulted to too low ram to run routing, DNS, and DHCP
3. Upgraded guest addons to fix drag and drop
4. Network Cards needed to be set up before launching vbox.
5. Had to fix issues with input on host and vbox, as well as allow bidirectional input, clipboards, and drag+drop


### Port forwarding