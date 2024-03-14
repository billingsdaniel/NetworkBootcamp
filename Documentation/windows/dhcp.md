# DHCP

## Contents:
1. Setting up DHCP
2. Using DHCP

## Setting up DHCP
In windows, we can use the GUI to set up DHCP on the host machine. We can also do it in Terminal with Powershell.
1. Open Terminal and start Powershell. Dont forget to run as administrator. \
`powershell`
2. Install DHCP server role \
`Install-WindowsFeature -Name DHCP -IncludeManagementTools`
3. Open MMC and snap in to DHCP
4. 