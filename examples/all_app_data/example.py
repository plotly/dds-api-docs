import csv
from gql import gql
from dds import client as dds_client
from datetime import datetime
from dateutil.parser import parse
import re
import pandas as pd

### GraphQL Querys
## Query individual app (can modify this query to grab whatever data you like)
apps_idv_app_query = gql(
    """
    query AppsQuery($name: String!, $allApps:Boolean!) {
        apps(name: $name, allApps: $allApps) {
            apps{
                name
                owner {username}
                analytics {dependencies {python}}
                analytics {timestamps {visited, updated, created}}
                analytics {resources {cpuUsage, memoryUsage, containerSize}}
                analytics {gitRevision {subject}}
                metadata {permissionLevel}
            }
        }
    }
    """
)

# Query all app names
apps_name_query = gql(
    """
    query AppsQuery($page: Int!, $allApps:Boolean!) {
        apps(page: $page, allApps: $allApps) {
            apps{
                name
            }
            nextPage
        }
    }
    """
)

### Get all app names
## Grabs all app names from server
def get_all_app_names():
    # Init constants
    app_names = []
    page = 0

    print("\nGetting all app names ...")

    # Run through all pages
    while page is not None:
        results = dds_client.execute(apps_name_query, {"page": page, "allApps": True})["apps"]

        resultApps = results["apps"]
        for result in resultApps:
            app_names.append(result['name'])
        page = results["nextPage"]

    print("\nCollecting list of app names ...")
    print("\nAll app names: ", app_names)
    return app_names


### Get individual application metadata
## Main function that gets all app names, meta data, and generates CSV
def get_all_apps_data():
    # Init constants
    all_app_names = get_all_app_names()
    all_app_data = []

    print("\nGetting metadata for all apps... ")

    # Run through all pages (recommend changing app_names to 1 - 5 apps for test Ex: all_app_names -> all_app_names[0:1])
    for app_name in all_app_names[0:2]:
        print("Querying: ", app_name)
        data = parse_idv_app_query(app_name)
        all_app_data.append(data)

    print("\nFinished!")
    return all_app_data


## Parse individual apps (can easily be modified for different queries)
def parse_idv_app_query(app_name):
    my_data = {}
    
    # Recursive function that parses through all nested dicts
    def meta_recur(node, name=""):
        for k, v in node.items():
            sep = "_"
            if name == "":
                sep = ""

            if isinstance(v, dict):
                meta_recur(v, name = name + sep + k)
            else:
                if v == None:
                    v = "None"
            
                my_data[name + sep + k] = v

    # DDS connection
    result = dds_client.execute(apps_idv_app_query, {"name": app_name, "allApps": True})[
        "apps"
    ]["apps"][0]
    
    # Call recursive function
    meta_recur(result)

    return my_data

## Generate CSV
def generate_csv(all_app_data):
    # Rearrange columns if name and owner_username exist
    df = pd.DataFrame(data=all_app_data)
    if {'name', 'owner_username'}.issubset(df.columns):
        df = df.reindex_axis(['name'] + ["owner_username"] + list(df.columns[:-1]), axis=1)
    print("\nGenerating CSV...")
    df.to_csv("./apps_data.csv", index=False)
    print("\nFinished!")
    return

def generate_df(all_app_data):
    df = pd.DataFrame(data=all_app_data)
    return df

# # Get all app data
# all_app_data = get_all_apps_data()

# # Create dataframe
# df = generate_df(all_app_data)
# print("\nDataframe: ", df.head(n=5))

# # Generate CSV
# generate_csv(all_app_data)