# removeEnvironmentVariable

## Mutation

```
mutation removeEnvironmentVariable($appname: String, $globalVar: Boolean, $name: String){
    removeEnvironmentVariable(appname: $appname, globalVar: $globalVar, name: $name){
        ok
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
error | `String`
