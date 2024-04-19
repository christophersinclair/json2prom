# json2prom
Convert POSTed JSON to PromQL Prometheus metrics to scrape.

This is useful in situations where your monitoring environment uses Prometheus to scrape data from components in the system where some components may not expose Prometheus metrics. Instead of building a custom Prometheus exporter for each different component, you can just post ANY JSON data you want to this and set this API as a Prometheus scrape target.

The logistics of setting this API up in a resilient way to ensure scrape target availability is an exercise left to the reader. It can run on Kubernetes, VMs, AWS ECS, CloudFoundry, laptop, whatever.


All API endpoints can be found at `<route>:41024/apidocs`

### Publishing Data to Convert (JSON POST)
```
curl -s -k -H "Content-Type: application/json" -X POST --data '{"metrics": [{"metric": {"metric_name": "http_200_response_count", "metric_value": "25", "metric_labels": [{"env": "prod"}]}}, {"metric": {"metric_name": "http_500_response_count", "metric_value": "2", "metric_labels": [{"env": "dev"}]}}]} http://<route>:41024/ingest
```

### Consuming Converted Data (Prometheus Scrape)
```
curl -s -k -H "Accept: text/plain" http://<route>:41024/metrics
```
