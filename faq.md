# MP12 FAQ

## MP context diagram: (Designed by students)
https://docs.google.com/drawings/d/16n-ll084RyDPXsXzRvz0RI1N02CT1VxtslrslhIqssk/edit

## Some useful commands:

```
kubectl get deployments -A --all-namespaces
kubectl get jobs -A --all-namespaces
kubectl describe <...>
kubectl get pods -A --all-namespaces
kubectl describe pod <pod_name> --all-namespaces
kubectl logs <...>
kubectl get nodes -A --all-namespaces
docker ps -a
docker container prune
docker images
```

## Deploying to cluster
- Created two job specs (one for free service and another one for premium)
- Tested job specs locally on node 0
- Defined ENV in job spec


## Also a few tips to save you some money in AWS. you can work in this order:
1. Containerize the classify.py first (you may need a t2.medium to build the image and test container, with ~20GB volume. You can change it back to t2.micro)
2. Develop the web application locally to expose image classification. (you can't test at this point just yet)
3. Configure EKS with 2 t3 medium nodes which will charge about ~ $0.2 / hour which you can 
4. Start and stop the cluster as you work on the MP / make changes.
5. Follow the minikube guide to develop against minikube locally, the server code will stay the same.


## I have set up Docker, Flask server etc. on my EC2 instance of educate starter account. Do I have to set it up again on my personal EC2 to access EKS?

No. You can access EKS through any system as far as you have configured aws credentials properly. 
https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

## How to access a worker node in EKS?

Type `kubectl get svc` and get the IP addresses of the worker nodes and then use ssh 
`kubectl get nodes`

## Do we have to create a new VPC?

Not required.

## am spending too much time on this MP. What should I do?
It is extremely important to have a conceptual understanding first and then try to approach this MP. 

## When I run my jobs, the status goes to ContainerCantRun. 
Use your path variables value and add it to the dockerfile. When you build the docker it will now include an updated path.

## The Docker image created to run the provided script lives on Docker Hub. Where exactly do Kubernetes live in our system? It can't be either of the 2 EC2 instances, right?
K8s acts as a container management tool. 

## From what I understand, Kubernetes just executes our Docker containers in a specific state, such as setting the Environment variables, correct?
K8s acts as a container management tool. 

## When we invoke Kubernetes in AWS, how will it know how to reach our EC2 instances?
You need to specify which image to deploy on k8s.

## What is the purpose of running 2 EC2 instances?
You need containers to run your applications.

## How to respond to MP’s grader GET and POST?
There is no code for the GET request. You are just hitting the endpoint to get the fields from each of your jobs as listed in the project description. 

## ModuleNotFoundError: No module named 'torch'?
-> RUN pip --no-cache-dir install torch torchvision in Dockerfile

## How to generate Free Service vs Default namespace?
You have to use generate-name or change the name dynamically.You cannot deploy the pod with the same name

## I cannot spawn any jobs on my free namespace with my resouce quote?
Ensure that you have specified the resources for your pods such that the cpu of your pods is capped at 0.9

## How do I delete all pods?
`kubectl delete --all all --namespace=free-service`

## How do I know if my resource quota is correct?
Verify your resource quota by checking that only 2 free-service jobs can be spawned at once. Also verify that any number of premium jobs can be spawned.

## My pods are not being created when I send the post request?
Verify you are using **generateName** instead of **name** in the metadata section.
Verfiy that you have specified resources for you job as well as for your resource quota.

## Can I execute kubectl shell commands from within my server instead of using the python API?
This method will be too slow and will cause the autograder to timeout. You should use the kubernetes python API directly.

## What should I tag my docker image as?
It is not recomended to use "latest", you should use an incremental tag 0.0.0, 0.0.1 etc. This will ensure that the kubernetes cluster isnt using an old cached version of latest.

## How should I use eksctl and kubectl?
It is recomended to spin up an EC2 instance that you will create and interact with your cluster from. You can also run your webserver from here.
