# json2prom
Convert POSTed JSON to PromQL Prometheus metrics to scrape.

This is useful in situations where your monitoring environment uses Prometheus to scrape data from components in the system where some components may not expose Prometheus metrics. Instead of building a custom Prometheus exporter for each different component, you can just post ANY JSON data you want to this and set this API as a Prometheus scrape target.

NOTE: This API hold all its information in-memory (NO persistent data storage). The design of this API assumes you have a Prometheus instance to scrape its metrics, therefore acting as the persistent datastore. So if this application restarts or dies (such as in a container or Pod), all of its knowledge of metrics is gone. You can simply post back to this API with more (or the same) data and it will keep it ready to serve again. Just keep in mind this design and use Prometheus to scrape and store the metrics, not `json2prom` itself.


All API endpoints can be found at `<route>:41024/apidocs`
![image](https://github.com/christophersinclair/json2prom/assets/29457515/75d65536-6905-4f21-9e24-8eef9b8ffaa1)


### Publishing Data to Convert (JSON POST)
```
curl -s -k -H "Content-Type: application/json" -X POST --data '{"metrics": [{"metric": {"metric_name": "http_200_response_count", "metric_value": "25", "metric_labels": [{"env": "prod"}]}}, {"metric": {"metric_name": "http_500_response_count", "metric_value": "2", "metric_labels": [{"env": "dev"}]}}]} http://<route>:41024/ingest
```

### Consuming Converted Data (Prometheus Scrape)
```
curl -s -k -H "Accept: text/plain" http://<route>:41024/metrics
```

#### Example
`http://<route>:41024/json` shows metrics already ingested in JSON format
![image](https://github.com/christophersinclair/json2prom/assets/29457515/a302097a-117d-45f2-bafb-44a68dbc5cc0)

`http://<route>:41024/metrics` shows metrics in Prom format

![image](https://github.com/christophersinclair/json2prom/assets/29457515/e6b2ce79-a11f-4bd8-926a-294d9fbd01e9)
