# json2prom
Convert POSTed JSON to PromQL Prometheus metrics to scrape.

All API endpoints can be found at `localhost:41024/apidocs`

### Publishing Data to Convert (JSON POST)
```
curl -s -k -H "Content-Type: application/json" -X POST --data '{"metrics": [{"metric": {"metric_name": "http_200_response_count", "metric_value": "25", "metric_labels": [{"env": "prod"}]}}, {"metric": {"metric_name": "http_500_response_count", "metric_value": "2", "metric_labels": [{"env": "dev"}]}}]} http://<route>:41024/ingest
```

### Consuming Converted Data (Prometheus Scrape)
```
curl -s -k -H "Accept: text/plain" http://<route>:41024/metrics
```