# unlinkService

## Mutation

```
mutation unlinkService($appname: String, $serviceName: String, $serviceType: ServiceType){
    unlinkService(appname: $appname, serviceName: $serviceName, serviceType: $serviceType){
        ok
        refresh
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
refresh | `Boolean`
error | `String`
