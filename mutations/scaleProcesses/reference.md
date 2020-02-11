# scaleProcesses

## Mutation

```
mutation scaleProcesses($appname: String, $processes: [ProcessInput]){
    scaleProcesses(appname: $appname, processes: $processes){
        ok
        refresh
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
appname | `String`
processes | `[ProcessInput]`

## Returns

Name | Type
---- | ----
ok | `Boolean`
refresh | `Boolean`
error | `String`
