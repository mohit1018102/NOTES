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









