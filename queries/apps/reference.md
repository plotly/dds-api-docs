# apps

## Query

```
query apps($page: Int, $name: String, $allApps: Boolean){
    apps(page: $page, name: $name, allApps: $allApps){
        apps{
            name
            owner{
                username
            }
            urlOnServer
            thumbnailUrl
            logs{
                app
                failed
            }
            collaborators{
                users
                teams
            }
            metadata{
                title
                description
                tags
                permissionLevel
                showInPortal
                sortRank
                contact{
                    name
                    email
                }
            }
            mounts{
                hostDir
                targetDir
                status
            }
            processes{
                type
                number
                status
            }
            analytics{
                timestamps{
                    created
                    updated
                    visited
                    error
                }
                gitRevision{
                    sha1
                    subject
                    error
                }
                resources{
                    cpuUsage
                    containersRunning
                    memoryUsage
                    memoryCapacity
                    imageSize
                    diskCapacity
                    containerSize
                    error
                }
                dependencies{
                    python
                    error
                }
                appname
            }
            environmentVariables{
                name
                value
                status
                readonly
            }
            linkedServices{
                name
                serviceType
                created
                status
            }
            status{
                running
                deploying
                canScale
            }
            resources{
                type
                status
                request{
                    cpu
                    memory
                }
                limit{
                    cpu
                    memory
                }
            }
        }
        nextPage
    }
}
```

## Arguments

Name | Type
---- | ---- 
page | `Int`
name | `String`
allApps | `Boolean`

## Returns

Name | Type
---- | ----
apps | `[App]`
nextPage | `Int`
