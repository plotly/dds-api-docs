# deleteWorkspace

## Mutation

```
mutation deleteWorkspace($appname: String){
    deleteWorkspace(appname: $appname){
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
