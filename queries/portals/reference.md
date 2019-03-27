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
            apps(page: $page){
                apps{
                    name
                    existsOnServer
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
                        isPublic
                        showInPortal
                        contact{
                            name
                            email
                        }
                    }
                    mounts{
                        hostDir
                        targetDir
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
                        existsOnServer
                    }
                    environmentVariables{
                        name
                        value
                        readonly
                    }
                    linkedServices{
                        name
                        serviceType
                        created
                    }
                    status{
                        running
                        deploying
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
