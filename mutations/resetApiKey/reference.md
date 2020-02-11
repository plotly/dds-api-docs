# resetApiKey

## Mutation

```
mutation resetApiKey($password: String){
    resetApiKey(password: $password){
        newKey
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
password | `String`

## Returns

Name | Type
---- | ----
newKey | `String`
error | `String`
