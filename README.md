# projectmlh (mobile local helper)

## Introduction :
Projectmlh is build for connecting people within a range. So that people work in unorganized sector of our economy, find work more easily & people who need helpers, then don't need to bother for that.
In todays era we have lots of online connection but few offline connection. Projectmlh going to help those people who need help/support in this modern era. 

eg : you are travelling in a city & you need someone as a companion. you can look for helpers it that locality, and then decide whether or not both of you want to travel together.


## Initialiation :

1. fork the repo
2. clone it
3. create your branch
4. python install
5. pip install `sudo apt install python3-pip`
6. install virtual environment : `sudo apt install python3.8-venv`
7. create virtual environment :`python3 -m venv venv`
8. Activate venv :`source venv/bin/activate` in root directory (mlh)
9. Django install : `sudo apt install python3-django`  
10. 9. Install the depepncies written in requirements.txt
11. Run application : `python3 manage.py runserver`

Or you can pull the docker image from DockerHub & deploy it on Minikube.

1. `docker pull parth721/django-mlh:<latest_tag_name>`
2. start minikube
3. `kubectl apply -f deployment.yaml`
4. `kubectl apply -f service.yaml`
5. `kubectl get deployments`
6. `kubectl get pods`
7. `kubectl get services`
8. `kubectl expose deployment <my-deployment> --type=NodePort --port=8080`
9. `minikube sevice <service-name> --url`

## Usage
user can register then login.After that, they can fill the form & submit to search for helpers.
