FROM redislabs/redistimeseries:1.0.3

CMD ["redis-server", "COMPACTION_POLICY", "max:1m:1d;min:1m:1d;avg:1m:1d", "RETENTION_POLICY", "60"]
