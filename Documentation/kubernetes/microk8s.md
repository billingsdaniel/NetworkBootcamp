# Kubernetes

## Kubernetes Concepts
Kubernetes is a system to keep plates spinning once they are in the air
### Object Types

1. Containers
Holds a specific app and its run environment
2. Pods
Holds containers that are all required to work together to function. These are templated together so when you scale up or down you are working at the pod level, such that you never have a container running without the other aps in containers around it requried for it to functon.
3. Deployments
Scales up or down on pods, uses templates to copy pods, monitors pod health, ect.
4. Services
How apps are accessed. Provides a static endpoint for when the app needs to be used by a client. Load balances what pods to call for that required outcome. 
5. Config maps
Allows you to update the configuration of a pod without rebuilding the pod from the ground up. May be attached as a file to the pod. Mostly used for environment variables or config files.
6. Secrets
Similar to config maps, but with separate access conditions for added security.

## Microk8s
openlens (3rd party ui) \
helm (third party tooling) \
.yml templating engine \
checking logs 