# addService

## Mutation

```
mutation addService($serviceType: ServiceType, $name: String){
    addService(serviceType: $serviceType, name: $name){
        service{
            name
            serviceType
            created
        }
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
service | `Service`
error | `String`
