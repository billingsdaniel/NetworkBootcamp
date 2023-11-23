helm repo add terraria https://www.seppevolkaerts.be/terraria-helm-charts/

You can then run helm search repo terraria to see the charts.

repo or git clone
values
helm upgrade --install


microk8s helm3 repo add \
          terraria \
          https://www.seppevolkaerts.be/terraria-helm-charts/

microk8s helm3 search repo terraria


look up kubernetes load balancer service with metallb

runnign on 7777 i want to expose it as a service of tuype load balancer sing metallb
how

microk8s kubectl apply -f file.yml

microk8s kubectl apply -f /home/vagrant/terraria-server/metallb-config.yaml