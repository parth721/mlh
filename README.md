# projectmlh (mobile local helper)

## Introduction :
### Problem : 
Domestic nursing care, especially after covid-19,also increase & often face difficulties finding rewarding & convienient opportunities. Patients onthe other hand, struggle to find available  helpers for in-home care need.

### Solution :
Projectmlh is build for connecting patients & nurses within the region of interest. So that people work in unorganized sector of our economy, find work more easily & people who need helpers, then don't need to bother for that. 

This user-friendly application is built on the Django framework, leverages Bootstrap for responsive design, and utilizes a SQLite database for data storage. Docker containerization ensures portability and simplifies deployment, while Minikube provides a local Kubernetes environment for development and testing.

![Screenshot from 2024-01-28 17-58-28](https://github.com/parth721/projectmlh/assets/112557191/c78378a2-1b0b-48d0-b992-67b8fff59be7)

### Prerequisites: 
1. Python 3.11
2. minikube
3. Docker 
4. Git(optional)
   
### For updating the project :  
1. fork the repo
2. clone it
3. setup virtual env :`python3 -m venv venv`  
4. Install the depepncies written in requirements.txt
5. test the changes : `python3 manage.py runserver`
6. start minikube
7. create or update the yaml files.
8. checks the status of pods, services, others
9. run the application in cluster : `minikube sevice <service-name>`
   
### For trying out:
you can pull the docker image from DockerHub & deploy it on Minikube. Follow the steps 1,2 then 6 to 9.

![Screenshot from 2024-01-29 10-10-15](https://github.com/parth721/projectmlh/assets/112557191/c1a8812e-0f51-467e-98b7-e2f71402046a)


## Usage
### 1. User registration & login
Users can register as either Patient or Helper accounts. Login credentials are required to access platform features.
### 2. Helpers profile creation
Helper users can create profiles outlining their skills, experience, qualifications, and availability.
### 3. searching for helpers
Patients can post requests specifying their care needs,availability timings. They can then search for matching Helper profiles based on various criteria.
### 4. communication
Patients can initiate communication with suitable Helpers to discuss requirements and arrange care bookings.
