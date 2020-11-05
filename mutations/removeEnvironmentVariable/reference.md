# removeEnvironmentVariable

## Mutation

```
mutation removeEnvironmentVariable($appname: String, $globalVar: Boolean, $name: String){
    removeEnvironmentVariable(appname: $appname, globalVar: $globalVar, name: $name){
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
globalVar | `Boolean`
name | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
refresh | `Boolean`
error | `String`
