"""
This code snippet demonstrates how to create and update a Gauge metric using the Prometheus Python client library.
"""
from prometheus_client import start_http_server, Gauge, CollectorRegistry, push_to_gateway
import time

# initialize start_time variable to record function starting time
start_time = time.time()


def test_push_to_gateway(value):
    """
    Start an HTTP server on port 8000 and set a gauge value of 100 to be sent on the server
    Args:
         gauge_metric: name of the gauge metric being created
         registry: name of the registry
    Returns:
       Returns a success message after successfully running for 100 seconds
    Raises:
          Server Creation Error with related error message
    """
    try:
        # Start an HTTP server on port 8000 and CollectorRegistry class to manage the registry of metrics.
        registry = CollectorRegistry()
        start_http_server(8002, registry=registry)

        # Create a Gauge metric
        gauge_metric = Gauge(
            'my_gauge_metric',
            'Test gauge metric',
            registry=registry)

        # Update the gauge metric value
        while True:
            # gauge_metric.set(value)  # Update the value
            gauge_metric.set(value)
            push_to_gateway('localhost:8002', job='test_job', registry=registry)
            time.sleep(1)  # Sleep for 1 second

            # exit the loop after 100 seconds
            if time.time() - start_time >= 100:
                break
        return "Successfully created prometheus server on port 8000"
    except Exception as e:
        print(str(e))


print(test_push_to_gateway(100))
