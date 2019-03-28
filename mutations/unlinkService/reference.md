# unlinkService

## Mutation

```
mutation unlinkService($appname: String, $serviceName: String, $serviceType: ServiceType){
    unlinkService(appname: $appname, serviceName: $serviceName, serviceType: $serviceType){
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
