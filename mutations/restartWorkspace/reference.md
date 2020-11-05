# restartWorkspace

## Mutation

```
mutation restartWorkspace($appname: String){
    restartWorkspace(appname: $appname){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
appname | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
