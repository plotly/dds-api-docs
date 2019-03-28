# removeCollaborators

## Mutation

```
mutation removeCollaborators($appname: String, $teams: [String], $users: [String]){
    removeCollaborators(appname: $appname, teams: $teams, users: $users){
        app{
            name
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
appname | `String`
teams | `[String]`
users | `[String]`

## Returns

Name | Type
---- | ----
app | `App`
error | `String`
