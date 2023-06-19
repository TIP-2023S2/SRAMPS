"""
This code snippet demonstrates how to create and update a Gauge metric using the Prometheus Python client library.
"""
from prometheus_client import start_http_server, Gauge
import time

start_http_server(8000)

# Create a Gauge metric
gauge_metric = Gauge('my_gauge_metric', 'Description of my gauge metric')

# Update the gauge metric value periodically
while True:
    gauge_metric.set(40)  # Update the value
    time.sleep(1)  # Sleep for 1 second