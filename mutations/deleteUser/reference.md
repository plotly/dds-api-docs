# deleteUser

## Mutation

```
mutation deleteUser($username: String){
    deleteUser(username: $username){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
username | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
