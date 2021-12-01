创建Cloudwatch event 规则

```
aws events put-rule --name GuardDuty-Medium-alert --event-pattern "{\"source\":[\"aws.guardduty\"],\"detail-type\":[\"GuardDuty Finding\"],\"detail\":{\"severity\":[4.0,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5.0,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,6.0,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9]}}" --region ap-northeast-1
```
创建SNS Topic

```
aws sns create-topic --name guardduty-alert-topic --region ap-northeast-1
```

订阅这个告警的Topic


```
aws sns subscribe --topic-arn arn:aws:sns:ap-northeast-1:accountID:guardduty-alert-topic --protocol email --notification-endpoint ####@qq.com --region ap-northeast-1
```

为Cloudwatch Event 规则的配置到SNS的目标

```
aws events put-targets --rule GuardDuty-Medium-alert --targets "Id"="1","Arn"="arn:aws:sns:ap-northeast-1:accountID:guardduty-alert-topic" --region ap-northeast-1
```

转换器

```json
{
    "time": "$.time",
    "region": "$.region",
    "instanceId": "$.detail.resource.instanceDetails.instanceId",
    "count": "$.detail.service.count",
    "severity": "$.detail.severity",
    "title": "$.detail.title",
    "description": "$.detail.description"
}
```

创建Cloudwatch event 规则

```
aws events put-rule --name GuardDuty-High-alert --event-pattern "{\"source\":[\"aws.guardduty\"],\"detail-type\":[\"GuardDuty Finding\"],\"detail\":{\"severity\":[7.0,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,8.0,8.1,8.2,8.3,8.4,8.5,8.6,8.7,8.8,8.9]}}" --region ap-northeast-1

```

