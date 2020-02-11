# addService

## Mutation

```
mutation addService($name: String, $serviceType: ServiceType){
    addService(name: $name, serviceType: $serviceType){
        service{
            name
            serviceType
            created
            status
        }
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
service | `Service`
error | `String`
