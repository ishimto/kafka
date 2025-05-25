# MONGODB && KAFKA && FLASK

## OVERVIEW
This repo contains helm templates for:
* Kafka - kafka-repo/kafka
* Kafka UI - obsidiandynamics/kafdrop
* MongoDB - bitnami/mongodb
* Shop-Web

## Prerequisites
Before deploying the Helm chart, ensure the following:


### Docker images

* Build and push the shop Docker image via [Dockerfile](https://git.infinitylabs.co.il/ilrd/haifa/hdo4/shoham.bozorgi/-/tree/main/devops/kafka/shop/python/Dockerfile) then update deployment [values](https://git.infinitylabs.co.il/ilrd/haifa/hdo4/shoham.bozorgi/-/blob/main/devops/kafka/shop/helm/values.yaml)

* Build and push the MongoDB consumer Docker image via [Dockerfile](https://git.infinitylabs.co.il/ilrd/haifa/hdo4/shoham.bozorgi/-/tree/main/devops/kafka/mongodb/consumer/Dockerfile) then update consumer [values](https://git.infinitylabs.co.il/ilrd/haifa/hdo4/shoham.bozorgi/-/blob/main/devops/kafka/mongodb/helm/values.yaml)

### Helm
Install [helm](https://helm.sh/docs/intro/install/)


### Deploy releases
Run [script.sh](https://git.infinitylabs.co.il/ilrd/haifa/hdo4/shoham.bozorgi/-/blob/main/devops/kafka/script.sh) using follow command: 

```
bash ./script.sh 
```

or:

```
chmod +x script.sh 
```

then:
```
./script.sh
```

### Prepare MongoDB
After the script finish to run and created the releases, you'll need to create db, collection and insert products using the following guide.

1.  Port Forwarding:

```
kubectl port-forward --namespace default svc/mongodb 43000:27017
```
2. Login Cluster

login using the default values if you didn't changed them

```
mongosh --host localhost:43000 -u root -p changeme --authenticationDatabase shop
```

3. Create Collection and Products

```
use shop
```

```
db.createCollection("products")
```

Now add products to your collection:

```
db.products.insertOne({name:"<your product name>"})
```

or look for insertMany, in order to avoid insert one by one :)


Congrats!! you are now shop owner.

## UI
Shop and Kafka UI

### Shop

```
kubectl get svc nginx-service
```

in minikube:

```
minikube service nginx-service
```

### Kafka

```
kubectl get svc kafdrop-svc
```

in minikube:

```
minikube service kafdrop-svc
```


* in this project the config maps are uploaded, in order to use it in your production, avoid to push it into your git with credentials.
  use .gitignore or some secret manager.


HAPPY HEALMING!!
