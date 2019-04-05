
# redisconf19-demo

## setup

docker-compose file from: https://github.com/RedisTimeSeries/prometheus-redistimeseries-adapter/tree/master/compose

To create specific downsampling rules and retention policy add the following command under `redis` service.
```
command: ["redis-server", "--loadmodule", "/usr/lib/redis/modules/redistimeseries.so", "COMPACTION_POLICY", "max:1m:1d;min:1m:1d;avg:1m:1d", "RETENTION_POLICY", "60"]
```

## Demos
1. weather station under `/weather_station`
2. Page view visitors counting under `/counters`
