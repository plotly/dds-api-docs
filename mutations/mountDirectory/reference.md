# mountDirectory

## Mutation

```
mutation mountDirectory($appname: String, $hostDir: String, $targetDir: String){
    mountDirectory(appname: $appname, hostDir: $hostDir, targetDir: $targetDir){
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
hostDir | `String`
targetDir | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
refresh | `Boolean`
error | `String`
