import csv
from gql import gql
from dds import client as dds_client
from datetime import datetime
from dateutil.parser import parse

### GraphQL Query
apps_page_query = gql(
    """
    query AppsQuery($page: Int!, $allApps:Boolean!) {
        apps(page: $page, allApps: $allApps) {
            apps{
                name
                analytics {timestamps {visited}}
                owner {username}
            }
            nextPage
        }
    }
    """
)

### Parse through apps_page_query results
def parse_query(query, page, all_developers, total_apps, latest_visit):
    # DDS connection
    result = dds_client.execute(apps_page_query, {"page": page, "allApps": True})[
        "apps"
    ]
    page += 1

    # Total apps
    total_apps = total_apps + len(result["apps"])

    # Current amount of apps in query
    app_count = len(result["apps"])

    # Check if nextPage
    next_page = result["nextPage"]

    for app_idx in range(app_count):
        # Parse for most recent visit
        recent_visit = result["apps"][app_idx]["analytics"]["timestamps"]["visited"]
        # Parse for owner of app
        developer = result["apps"][app_idx]["owner"]["username"]
        # Save only unique developers (no duplicates)
        if developer not in all_developers:
            all_developers.append(developer)
        # Parse for latest visit
        if recent_visit is None:
            continue
        else:
            latest_visit = max(latest_visit, parse(recent_visit))

    return {
        "result": result,
        "page": page,
        "all_developers": all_developers,
        "total_apps": total_apps,
        "latest_visit": latest_visit,
        "next_page": next_page,
    }


### Generate a CSV
def generate_csv(all_developers, total_apps, latest_visit):
    data = [{
        "Total Developers": len(all_developers),
        "Total Apps": total_apps,
        "Latest Visit": str(latest_visit),
    }]

    with open('dds_data.csv', 'w') as csvFile:
        fields = ["Total Developers", "Total Apps", "Latest Visit"]
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
    csvFile.close()

### Loop through all apps on DDS server and return relevant meta data
def get_meta_data():
    # Init constants
    all_developers = []
    total_apps = 0
    latest_visit = datetime(year=2000, month=1, day=1)
    page = 1

    print("\nRunning... ")

    # Run through all pages
    while page is 1 or next_page is not None:
        data = parse_query(
            apps_page_query, page, all_developers, total_apps, latest_visit
        )
        all_developers = data["all_developers"]
        page = data["page"]
        total_apps = data["total_apps"]
        latest_visit = data["latest_visit"]
        result = data["result"]
        next_page = data["next_page"]
    
    print("\nSample Query (Last Query): ", result)
    print("\nTotal Apps: ", total_apps)
    print("\nLatest Visited App Time: ", latest_visit)
    print("\nTotal Developers: ", len(all_developers))
    print("\nDeveloper Usernames: ", all_developers)

    print("\nGenerating CSV...")
    generate_csv(all_developers, total_apps, latest_visit)

get_meta_data()
