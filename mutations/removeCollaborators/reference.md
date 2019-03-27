# removeCollaborators

## Mutation

```
mutation removeCollaborators($teams: [String], $users: [String], $appname: String){
    removeCollaborators(teams: $teams, users: $users, appname: $appname){
        app{
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
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
teams | `[String]`
users | `[String]`
appname | `String`

## Returns

Name | Type
---- | ----
app | `App`
error | `String`
