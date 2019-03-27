# changePassword

## Mutation

```
mutation changePassword($currentPassword: String, $newPassword: String){
    changePassword(currentPassword: $currentPassword, newPassword: $newPassword){
        ok
        currentPasswordError
        newPasswordError
    }
}
```

## Arguments

Name | Type
---- | ---- 
currentPassword | `String`
newPassword | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
currentPasswordError | `String`
newPasswordError | `String`
