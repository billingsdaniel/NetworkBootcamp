Vagrant.configure("2") do |config|
  # Configuration for VM 1
  config.vm.define "VB_Router" do |vm1|
    vm1.vm.box = "gusztavvargadr/ubuntu-desktop"
    vm1.vm.network "public_network", type: "dhcp"
    vm1.vm.network "private_network", ip: "192.168.1.1", virtualbox__intnet: true
    vm1.vm.provider "virtualbox" do |vb1|
      vb1.memory = "3072"
    end
  end

  # Configuration for VM 2
  config.vm.define "VB_1" do |vm2|
    vm2.vm.box = "gusztavvargadr/ubuntu-desktop"
    vm2.vm.network "private_network", type: "dhcp", virtualbox__intnet: true
    vm2.vm.provider "virtualbox" do |vb2|
      vb2.memory = "2048"
    end
  end
end