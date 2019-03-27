# updateSshKeys

## Mutation

```
mutation updateSshKeys($keys: String){
    updateSshKeys(keys: $keys){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
keys | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
