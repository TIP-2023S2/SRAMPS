# Prometheus Client Setup and Usage
## Installation
```shell
$ pip3 install prometheus-client 
```

## Usage
Even though there are several use cases of prometheus client, we will be going through modules specifically used in the project.

### `GAUGE`
Gauge is one of the metric type that can arbritarily go up or down.
It is typically used to measure a current value or a snapshot of a 
value at a particular moment. Examples of Gauge metrics can include
the current number of active users, the amount of free disk space,
or the current temperature.

In simple words, take gauge like an accelerometer on a car. The value can
go up or down depending on how fast the car is moving. One difference is that
you can set a fixed value to a gauge.

#### Usage of GAUGE

```HTML
gauge.set(value) -> Sets the value of the Gauge to the specified value.
gauge.inc(value=1) -> Increments the Gauge value by the specified amount (default is 1).
gauge.dec(value=1) -> Decrements the Gauge value by the specified amount (default is 1).
gauge.set_to_current_time() -> Sets the Gauge value to the current timestamp.
```
In XC3, `GAUGE` is used to store user information such as "user_name", "user_arn", "user_id", "account_id"
"Query_Time", "user", "region", "resources_cost"
and push the data to Prometheus

### `Collector Registry`
In `Prometheus`, a `CollectorRegistry` is an object that is responsible for collecting and managing all the
metric collectors in a Prometheus client application.

In `XC3`, the data collected and stored in `Gauge` is stored in a `CollectorRegistry` 
The CollectorRegistry serves as a central component for managing and organizing metrics
in a Prometheus client application, enabling easy registration and collection of metrics for further analysis and monitoring.

### `Push_to_gateway`
The `push_to_gateway` feature allows you to push metrics from a non-Prometheus server or job to the Prometheus server. 
It is useful in scenarios where you have short-lived or ephemeral jobs that cannot be scraped by the Prometheus server directly.

In `XC3` `push_to_gateway` is used to send the data from short lived lambda functions 
to the prometheus server.


### Collective usage
```python
push_to_gateway(
            os.environ["prometheus_ip"],
            job="IAM_User_Resource_List_Cost_" + regionName,
            registry=registry,
        )
        push_to_gateway(
            os.environ["prometheus_ip"],
            job="IAM_User_Total_Services_Cost_List_" + regionName,
            registry=registry,
        )
```

In the above example code snippet taken from `XC3`, `push_to_gateway`
is being used to send the data collected from `IAM_User_Resource_List_Cost_` and 
`IAM_User_Total_Services_Cost_List_` lambda functions and is sent to the 
prometheus server.

To further break it down
```json lines
The data returned from lambda function is stored in GAUGE.
The data collected in GAUGE is sent to the Collector Registory.
The aggregated data is sent to prometheus server using push_to_gateway.
```