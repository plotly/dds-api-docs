# All App Data Example
## Context
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



## Usage
Ensure that you populate the `dds.py` file with a DDS account that has access to all applications on the server, and the correct endpoint.

Add/remove queries by modifying the variable `apps_idv_app_query` in `example.py` with your own custom queries.