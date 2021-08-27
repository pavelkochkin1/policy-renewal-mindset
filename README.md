# My research of classification policy renewal and deployment of model to app. 
[for mindset](http://mind-set.ru/)

## About project

## To-do list

- [x] Create model
- [x] Model pipeline
- [x] Model ready to inference
- [x] App for load data and make prediction
- [x] Downloading prediction
- [ ] Make app container
- [ ] Make the output of the final table in html on the site

## How to run:
1. Install and run Docker
2. Build Docker image using `docker build . -t policy_server`
3. Run Docker container using `docker run --rm -it -p 8888:8888 policy_server`
4. Go to `http://localhost:8888/`

## Source code
* [research/](research/) contains my data and model research
* [app.py](app.py) contains server logic
* [model/model.py](model/model.py) class of model
* [data/data.txt](data/data.txt) - initial data
* [data/data.csv](data/data.csv) - clear and "to numeric" data
* [templates](templates/) and [static](static/) includes html and css files for app
* [Dockerfile](Dockerfile) describes a Docker image that is used to run the app

## Example