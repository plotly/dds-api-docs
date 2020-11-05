# portals

## Query

```
query portals($page: Int, $page1: Int, $name: String){
    portals(page: $page1, name: $name){
        portals{
            id
            name
            logoUrl
            metadata
            requireLogin
            apps(page: $page){
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
        nextPage
    }
}
```

## Arguments

Name | Type
---- | ---- 
page | `Int`
page | `Int`
name | `String`

## Returns

Name | Type
---- | ----
portals | `[PortalObject]`
nextPage | `Int`
