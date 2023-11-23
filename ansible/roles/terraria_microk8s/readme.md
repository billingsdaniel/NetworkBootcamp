helm repo add terraria https://www.seppevolkaerts.be/terraria-helm-charts/

You can then run helm search repo terraria to see the charts.

repo or git clone
values
helm upgrade --install


microk8s helm3 repo add \
          terraria \
          https://www.seppevolkaerts.be/terraria-helm-charts/

microk8s helm3 search repo terraria