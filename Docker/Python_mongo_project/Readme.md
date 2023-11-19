# Build & Run steps
### step 1: build src/ dockerfile to generate image

``` cmd
docker build -t my_python_app:2.0 . 
```
### step 2: run compose file

``` cmd
docker-compose -f compose.yaml up -d
```
