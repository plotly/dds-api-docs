# removeEnvironmentVariable

## Mutation

```
mutation removeEnvironmentVariable($globalVar: Boolean, $name: String, $appname: String){
    removeEnvironmentVariable(globalVar: $globalVar, name: $name, appname: $appname){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
globalVar | `Boolean`
name | `String`
appname | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
