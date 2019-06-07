FROM redislabs/redistimeseries:latest

CMD ["redis-server", "--loadmodule", "/usr/lib/redis/modules/redistimeseries.so", "COMPACTION_POLICY", "max:1m:1d;min:1m:1d;avg:1m:1d", "RETENTION_POLICY", "60"]
