# unmountDirectory

## Mutation

```
mutation unmountDirectory($appname: String, $hostDir: String, $targetDir: String){
    unmountDirectory(appname: $appname, hostDir: $hostDir, targetDir: $targetDir){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
appname | `String`
hostDir | `String`
targetDir | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
