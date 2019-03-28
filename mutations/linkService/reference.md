# linkService

## Mutation

```
mutation linkService($appname: String, $serviceName: String, $serviceType: ServiceType){
    linkService(appname: $appname, serviceName: $serviceName, serviceType: $serviceType){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
appname | `String`
serviceName | `String`
serviceType | `ServiceType`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
