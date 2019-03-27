# mountDirectory

## Mutation

```
mutation mountDirectory($targetDir: String, $hostDir: String, $appname: String){
    mountDirectory(targetDir: $targetDir, hostDir: $hostDir, appname: $appname){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
targetDir | `String`
hostDir | `String`
appname | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
