# Prometheus Architecture

## Three parts:
1. Time-Series Database which stores metrics and log data
2. Retrieval which pulls metrics data from targets
3. HTTP server which accepts queries such as PromQL to expose those data

## Metrics:
* Human-Readable format
* Each entries have two parts:
    1. HELP: description of the metrics
    2. TYPE: 3 metric types
        * Counter: how many times X happened?
        * Gauge: what is the current value of X?
        * Histogram: how long or how big is X?

## How to collect those metrics?

* Either, Each target exports “/metrics” endpoint from which prometheus’ data retrieval worker pulls the metrics. (data must be in correct format)

* Or, Many services don’t expose this endpoint, so, needs another component known as exporter.
There is a exporter’s list in [Prometheus site](https://prometheus.io/docs/instrumenting/exporters/).
Exporters fetch metrics from those targets, converts to correct format and exposes its own “/metrics” endpoint.

Prometheus pulls data, so, it pulls data from time to time which is better in comparison to some monitoring systems like Cloud Watch which relies on the targets pushing the data.
* High load of network traffic
* Monitoring can be the bottleneck
* Install additional software or daemon on each target to push the metrics
* Instead, if it is pull based, different prometheus instances can pull metrics data
* Also, better detection/insight on if service is up and running or not

## Pushgateway:
Some cron or batch or scheduled jobs may not be long around for data to be scraped by prometheus. For such jobs, they push their metrics to PushGateway at exit and then, prometheus server can pull data from pushgateway whenever it is scheduled to do so.

## prometheus.yml:
* Which targets to scrape?
* At what interval?

The file has:
1. Global
    * Scrape_interval: how often to scrape the data
    * Evaluation_interval: How often to run the rules
2. Rule_files:
    * Aggregating data
    * Creating alerts when certain condition is met
3. Scrape_configs:
    * What resources it monitors?

## AlertManager:
Prometheus Server pushes alerts to AlertManager and then, alertmanager can notify through email, slack, etc.

## PromQL:
Prometheus Web UI or more powerful tools like Grafana uses PromQL to fetch the data from Prometheus and show the data.
