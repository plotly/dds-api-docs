# deleteApp

## Mutation

```
mutation deleteApp($name: String){
    deleteApp(name: $name){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
name | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
