"""
This code snippet demonstrates how to create and update a Gauge metric using the Prometheus Python client library.
The code imports the necessary modules from the Prometheus client library. It includes the start_http_server function
to start an HTTP server on port 8000, the Gauge class to create a Gauge metric, and the CollectorRegistry class to
manage the registry of metrics
"""

from prometheus_client import start_http_server, Gauge, CollectorRegistry
import time

# initialize start_time variable to record function starting time
start_time = time.time()


def test_registry(value):
    """
    Start an HTTP server on port 8000 and the registry object to start an HTTP server that exposes the metrics
    registered in the registry.
     Args:
          gauge_metric: name of the gauge metric being created
          registry: name of the registry
    Returns:
         Returns a success message after successfully running for 100 seconds Raises: Server Creation Error with related
                error message
    """
    try:
        # Start an HTTP server on port 8000 and CollectorRegistry class to manage the registry of metrics.
        registry = CollectorRegistry()
        start_http_server(8000, registry=registry)

        # Create a Gauge metric
        gauge_metric = Gauge(
            'my_gauge_metric',
            'Test gauge metric',
            ['label_name1', 'label_name2'],
            registry=registry)

        # Update the gauge metric value
        while True:
            gauge_metric.labels(label_name1='value1', label_name2='value2').set(value)  # Update the value
            time.sleep(1)  # Sleep for 1 second

            # exit the loop after 100 seconds
            # if time.time() - start_time >= 100:
            #     break

    except Exception as e:
        print(str(e))

    return "Successfully created prometheus server on port 8000"


print(test_registry(100))

