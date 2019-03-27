# uploadPortalLogo

## Mutation

```
mutation uploadPortalLogo($page: Int, $logo: Upload!, $portalname: String){
    uploadPortalLogo(logo: $logo, portalname: $portalname){
        portal{
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
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
page | `Int`
logo | `Upload!`
portalname | `String`

## Returns

Name | Type
---- | ----
portal | `PortalObject`
error | `String`
