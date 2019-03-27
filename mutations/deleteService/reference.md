# deleteService

## Mutation

```
mutation deleteService($serviceType: ServiceType, $name: String){
    deleteService(serviceType: $serviceType, name: $name){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
serviceType | `ServiceType`
name | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
