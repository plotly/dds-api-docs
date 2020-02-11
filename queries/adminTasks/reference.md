# adminTasks

## Query

```
query adminTasks{
    adminTasks{
        tasks{
            sourceUsername
            targetUsername
            taskName
            taskStatus
        }
    }
}
```

## Returns

Name | Type
---- | ----
tasks | `[AdminTask]`
