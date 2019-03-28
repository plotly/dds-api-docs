# deleteService

## Mutation

```
mutation deleteService($name: String, $serviceType: ServiceType){
    deleteService(name: $name, serviceType: $serviceType){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
name | `String`
serviceType | `ServiceType`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
