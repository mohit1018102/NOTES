# Docker
1. Docker is a virtualization tool, which virtualise the Application component of the Os and uses  Host's Kernel.<br>
2. Docker pakage project , its dependency into portable artifact. So that it can easily share among developeres, tester, operation team.

## System Layout
                ----------------
                  APPLICATION    [layer-1] : Application layer means different UI : eg ubuntu, kali linux
                ----------------
                    KERNEL       [layer-2] : kernel helps Application layer to communicate with hardware
                -----------------
                    HARDWARE     [layer-3] :  physical components.
                -----------------

| Docker                                             |  virtual machine|
|:---------------------------------------------------|:--------------------------------------------:|
| Virtualize Application layer                       | Virtualize kernel+application layer          |
| startup time is less :no booting uses host's kernel|  startup time is more bcz of booting         |
| size is small in mbs                               | size is big in Gbs                           |
| Compability issues are there ex if host doesn,t support linux it won't work| no compability issue because of its own kernel|

## Image 
1. Image is packed version of your application or dependency : portable artifact
2. Can be found in DockerHub, or private repos like aws ECR.

## Container
1. Container is a running environment for IMAGE.
2. Contains Layer of images
3. Mostly based on Linux Base image, because of small size eg: apline

   ### layout
   
         ------------------------------------------------------------
               Application images -> MongoDb, Mongo-express
         ------------------------------------------------------------
                   Intermediate images
         ------------------------------------------------------------
             Linux base image : alpine:3.10
         ------------------------------------------------------------

**Docker contains Containers contains images contains dependencies or requirements.**

## Application Development
Eg : An application required MongoDb and nodejs for an application.
<br>Developer : 4<br>
### Before containers
1. Everyone has to install all the dependencies and it might be possible that there are some variation in that process.
2. Result_possibility:
     *  Ok Runs perfectly
     *  or Might get dependency issues
3. these problem might slow down the process


### After Containers
**Dev1** --> create a image containing all the dependencies and push to the ---> **Registry**<br>
**Dev 2,3,4**-> will pull the image from the registry and start working on it.<br>
**only one has to install everything.**

----
## Application Deployment

#### Before Container
1. Dev team pass App + build_document to operation team.
2. operation team read the document and deploy the application.
3. Possibilty :
   * might install wrong version of dependencies.
   * might misunderstood the build_document.
   * or dev team missed few steps in documents
   * everything result in a delay.

### After Container
**Dev team** creates a image ------> push to----> **Registery**  <------pulled by operation team and deploy.<br> 

# DOCKER COMMANDS
1. **Docker Pull** pull image to the local machine.
  ```cmd
  docker pull <image_name>
  ```
2. **Docker create** : create a container w/o starting it.
  ```cmd
    docker create <image_name>
   ```
3. **Docker Start:** start the container
  ```cmd
      docker start <image_name>
  ```
4. **Docker Stop:** start the container
  ```cmd
      docker stop <image_name>
  ```
    
5. **Docker run --> creates and run Docker container** from image (**docker pull+docker create + docker start**)
* creates container and run in normal mode ( close on exit)
  ```cmd
  docker run <image_name>
  ```
* creates and run image in dettach mode (you have to use Docker stop to stop the container)
  ```cmd
  docker run -d <image_name>
  ```
* naming of container
  ```cmd
  docker run --name mongodb mongo
  ```
* port configuration : we have to link container port to host port inorder to access container from host
  ```cmd
     docker run -d -p host_port:container_port --name <custom_name> <image_name>
  ```
* **Container Network**: Container inside same  network can be liked using container name.
  ```cmd
   docker network create <custom_network>
   docker run -d -p host_port:container_port --name <custom_name> --net <custom_network>  <image_name>
  ```
**Note : -e Env_variable=xyz**

6. **docker logs** : to display log
   ```cmd
       docker logs <container_id/name>
    ```
7. To get **container terminal**
     ```cmd
       docker exec -it <cointainer_id/name> /bin/bash
     ```

      ```cmd
       docker exec -it <cointainer_id/name> /bin/sh
     ```
 8. list containers
    * list running containers 
    ```cmd
        docker ps
     ```
     * list all containers 
     ```cmd
        docker ps -a
     ``
  10. list all images
      ```cmd
          docker image ls
      ```
  11. remove container
      ```cmd
          docker remove <image_name/id>
      ```
12. remove image
      ```cmd
          docker rmi <image_name>
      ```
# Docker-Compose
Structured container commands for access.

### create a network
```cmd
 docker network create mongo-network
```
### setup mongodb container
```cmd
docker run -d \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=password \
--name mongodb \
--net mongo-network \
mongo
```
### setup mongodb-express container

  ```cmd
docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
--net mongo-network \
-- name mongo-express \
mongo-express
```

### compose.yaml : will create seperate network by default using project name
```yaml
version: '3'
services:
  mongodb:
    image: mongo
    ports:
    - 27017:27017
    environment:
    - MONGO_INITDB_ROOT_USERNAME=admin
    - MONGO_INITDB_ROOT_PASSWORD=password
  mongo-express:
    image: mongo-express
    ports:
    - 8080:8081
    environment:
    - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
    - ME_CONFIG_MONGODB_ADMINPASSWORD=password
    - ME_CONFIG_MONGODB_SERVER=mongodb
```

### command to use compose.yaml
* **start the containers**
  ```cmd
    docker-compose -f compose.yaml up -d
  ```
* **stop the containers**
  ```cmd
    docker-compose -f compose.yaml down 
  ```

  ## Building image from project
  ### server.js
  ```js
        const http=require("http");
        const host = 'localhost';
        const port = 8000;
        const requestListener = function (req, res) {
              res.writeHead(200);
              res.end("My first server 1.0!");
         };

        const server = http.createServer(requestListener);
        server.listen(port, host, () => {
            console.log(`Server is running on http://${host}:${port}`);
        });
  ```
  ### Dockerfile
  ```dockerfile
    FROM node:13-alpine
    ENV MONGO_DB_USERNAME=admin 
    ENV MONGO_DB_PWD=password
    RUN mkdir -p /home/project
    COPY . /home/project
    CMD ["node","/home/project/server.js"]
  ```

  ### commands to build
  ```cmd
     docker build -t my_app:1.0 .
  ```

  









