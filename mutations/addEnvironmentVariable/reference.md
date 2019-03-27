# addEnvironmentVariable

## Mutation

```
mutation addEnvironmentVariable($globalVar: Boolean, $name: String, $value: String, $appname: String){
    addEnvironmentVariable(globalVar: $globalVar, name: $name, value: $value, appname: $appname){
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
value | `String`
appname | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
