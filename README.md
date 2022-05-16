# Dandelion
In this application, the user can send their desired text to a particular phone number and/or email address.

# Technologies used
* Python3
* Django4
* Djangorest
* Celery
* Redis
* Docker

# Installation
* install Docker

  You must install Docker to run Redis container on it.

  Pay attention that in this project we're using Kavenegar API to send text.

**1. clone the project**
  ```
  git clone git@github.com:Manaa94/Dandelion.git
  ```
**2. move '.env-sample' to the path Dandelion/, rename it to '.env', and provide required variables.**
  ```
  mv .env-sample Dandelion/.env  
  ```
  
**3. create a python virtual environment**
  ```
    python3 -m venv venv
  ```
**4. activate your venv**
on linux and mac
  ```
    source venv/bin/activate
  ```
on windows
  ```
    venv/Scripts/activate
  ```
**5. install requirements**
  ```
    pip install -r requirements.txt
  ```
**6. run a redis container on docker**
  ```
  docker run -p 6379:6379 --name my-redis -d redis
  ```
**7.run a celery worker in a seprated terminal tab**
  ```
  celery -b redis://localhost:6379 -A api.tasks worker -E -Q send --loglevel INFO
  ```

**8. migrate**

**9. run the project**
