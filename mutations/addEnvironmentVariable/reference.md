# addEnvironmentVariable

## Mutation

```
mutation addEnvironmentVariable($appname: String, $globalVar: Boolean, $name: String, $value: String){
    addEnvironmentVariable(appname: $appname, globalVar: $globalVar, name: $name, value: $value){
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
value | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
refresh | `Boolean`
error | `String`
