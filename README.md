# Test BigQuery Python Client Library

I've created a very simple example to follow a long. First a couple of things to know:

1. I am not a python developer so this may not be organized well, but I am trying to learn and appreciate feedback. My job is to provide engineering support to data scientists. It's a new world for me, my background is in sysadmin, containerization, hosting web apps, and a lot of k8s. I've followed SOME portions of a successful workflow I helped develop for our team using Docker and Makefile targets to simplify the process and abstract away the "hard stuff" about docker our data scientists don't have experience with. 

2. This readme assumes you're sane and can handle package management. Kenneth Reitz is awesome, Pipenv is garbage. Use requirements.txt

3. This readme assumes you're sane and working in linux/unix. If you need Windows support, get at me and I'll help. But I don't want to cross that bridge until it's necessary.

## Using this workflow

1. Create a dataset in bigquery, feel free to use the data in [data.csv](./data.csv) to populate a table, or just use what you have already (you'll need to modify the query in __main__.py)

2. Create a service account key and save it in this directory as creds.json

3. Grant that service account the following roles:

4. If you're on Linux/Unix and have docker installed: `make docker.run` will build a container, run it, and drop you into a bash environment with python 3.7. Adjust your python environment accordingly by changing the FROM field in the [Dockerfile](./Dockerfile)

5. Activate the service account: `gcloud auth activate-service-account --keyfile=/bq_test/creds.json && gcloud config set project <your gcloud project id>

6. To run the test you must supply the path of your bigquery table to the python script like so: `python __main__.py <dataset_name>.<table_name>`

## I have python installed and just want to run the test

1. `export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service/account/key/file`

2. `gcloud config set project <project_id>`

3. `pip install -r requirements.txt`

4. `python __main__.py <dataset_name>.<table_name>`