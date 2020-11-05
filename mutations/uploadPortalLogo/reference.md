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
            requireLogin
            linkFromPortalToAppManager
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
                    hasWorkspace
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
                            gpu
                            memory
                        }
                        limit{
                            cpu
                            gpu
                            memory
                        }
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
