# Simple Dash UI for GraphQL Queries

This app demonstrates how to use Celery and Redis to trigger GraphQL queries, set/get timestamps, and view the query data in a `dash-table`.

![Screenshot from 2019-08-29 11-23-13](https://user-images.githubusercontent.com/33464965/63953550-8a1e9d00-ca4f-11e9-843c-66b148d09527.png)

## Instructions (Local)
1. Populate your Redis DB: `python3 predeploy.app`.
2. Start Celery worker and beat (see instructions below in Celery and Redis section).
2. Run Dash app: `python3 app.py`.

### Usage
Ensure that you populate the `dds.py` file with a DDS account that has access to all applications on the server, and the correct endpoint.

Add/remove queries by modifying the variable `apps_idv_app_query` in `example.py` with your own custom queries.

## File Directory 

* `app.json`: Configuration file for running predeploy scripts on DDS.
* `predeploy.py`: Predeploy script that runs GraphQL query and populates Redis DB.
* `index.py`: Main entry point into Dash application and router.
* `tasks.py`: Redis & Celery instances and methods.
* `app.py`: Dash app.
* `dds.py`: DDS GraphQL credentials.
* `example.py`: Contains GraphQL query script that can also be used to generate a   `.csv` and `df`.

## GraphQL Query 
### Context
This application will return *user specified* meta data for all applications on the DDS server.

It works by grabbing all DDS application names on the server, and than individually querying against each app with your custom queries (for speed).

A recursive function traverses through the returned query from DDS, 
and a `.CSV` with the name `apps_data.csv` is generated.

Note: It may take a while to query all your applications depending on how many you have.

By default the following queries will be called:
```
name
analytics {dependencies {python}}
analytics {timestamps {visited, updated, created}}
analytics {resources {cpuUsage, memoryUsage, containerSize}}
analytics {gitRevision {subject}}
metadata {permissionLevel}
``` 
## Redis/Celery Setup
### Linux/MacOS:

#### Running the Redis-Server
* First off you need a Redis instance. A simple way to do this, if you have docker locally, is to run a Redis container:
`docker run --name local-redis -d redis`

Then:
`docker inspect local-redis | grep IPAddress` to get your Redis instance's IP address

* If you don't have docker, alternatively, see the Redis documentation: https://redis.io/documentation to download Redis and set up a local instance.

#### Runing the Redis & Celery Instance
The next commands need to be running from the root of your Dash App (Where the files `app.py` and `tasks.py` are)

* The scheduler:
`celery -A tasks beat --loglevel=DEBUG`

* The worker that will actually run the tasks:
`celery -A tasks worker --loglevel=DEBUG`

* The dash app:
`python app.py`

### Windows:
Redis is not optimized to work with Windows, but it is possible to use it. 

#### Running the Redis-Server
1. Download the Redis MSI installer for Windows from https://github.com/MicrosoftArchive/redis/releases & run the MSI installer.

2. Install Redis Python Client with `pip install redis`. 
Note: Originally I had used version `2.10.6` which gave a lot of errors. Upgrading to version `3.2.1` fixed these issues. For more information about the Python client go here: https://redislabs.com/lp/python-redis/

3. Open the cmd and go to the root directory of Redis. Run `redis-server` in cmd. If you get an error check the troubleshooting portion below.  

#### Runing the Redis & Celery Instance
**Note: Ensure you're running the below commands in a terminal such as Git Bash or Cygwin**
* The Redis db (run in root of Redis folder or have in Windows ENV variables):
`redis-server`

* The scheduler:
`celery -A tasks beat --loglevel=DEBUG`

* The worker that will actually run the tasks (ensure you have `gevent` -> `pip install gevent`):
`celery -A tasks worker --loglevel=DEBUG info -P gevent`

* The dash app:
`python app.py`

At the end of it you will have four terminals open in total.

#### Troubleshooting (Windows)
If you see the error: `Can't bind TCP listener *:6379 using Redis on Windows`
Follow these steps: 
1. `cd` to the bin directory of Redis, and run
2. `redis-cli`
3. `shutdown`
4. `exit`
5. Open another cmd window, cd to the directory of your Redis installation, and run in cmd `redis-server`.
More information on this error here: https://stackoverflow.com/questions/31769097/cant-bind-tcp-listener-6379-using-redis-on-windows

## Dash Deployment Server
This application code is deploy-ready. You will simply need to create & link a Redis database on Dash Deployment Server and then deploy using the standard git push plotly master commands.