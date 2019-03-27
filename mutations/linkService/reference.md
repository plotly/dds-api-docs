# linkService

## Mutation

```
mutation linkService($serviceType: ServiceType, $serviceName: String, $appname: String){
    linkService(serviceType: $serviceType, serviceName: $serviceName, appname: $appname){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
serviceType | `ServiceType`
serviceName | `String`
appname | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
