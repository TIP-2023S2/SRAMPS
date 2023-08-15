"""
This code snippet demonstrates how to create and update a Gauge metric using the Prometheus Python client library.
"""
import boto3
from datetime import date, timedelta
from prometheus_client import start_http_server, Gauge, CollectorRegistry, push_to_gateway
import time

# initialize required variable/dependencies
account = boto3.client("sts", region_name="eu-west-1")
account_id = account.get_caller_identity()['Account']
region = "eu-west-1"

end_date = str(date.today())
start_date = str(date.today() - timedelta(days=30))

# initialize start_time variable to record function starting time
start_time = time.time()


def getAccounts():
    client = boto3.client('ce')
    response = client.get_cost_and_usage(
        TimePeriod={"Start": start_date, "End": end_date},
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[{"Type": "DIMENSION", "Key": "LINKED_ACCOUNT"}],
    )

    print(response)
    cost = response["ResultsByTime"][0]["Groups"]
    print(cost)
    sorted_cost_data = sorted(
        cost,
        key=lambda x: x["Metrics"]["UnblendedCost"]["Amount"],
        reverse=True,
    )
    # print(sorted_cost_data)
    return sorted_cost_data


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
        # Start an HTTP server on port 8002 and CollectorRegistry class to manage the registry of metrics.
        registry = CollectorRegistry()
        # start_http_server(8002, registry=registry)

        array = []
        json_data = []

        data = getAccounts()

        for item in data:
            resources = {
                "service": item["Keys"][0],
                "cost": item["Metrics"]["UnblendedCost"]["Amount"]
            }
            array.append(resources)

        print(array)

        # Create a Gauge metric
        gauge_metric = Gauge(
            'My_USED_SERVICES_DETAILS',
            'AWS services with cost',
            labelnames=["service", "cost"],
            registry=registry)

        # format data into dict
        for each in range(len(array)):
            service = array[each]["service"]
            cost = array[each]["cost"]
            data_dict = {"service": service, "cost": cost}

            json_data.append(data_dict)
            gauge_metric.labels(service, cost).set(cost)
        print("JSON DATA =>", json_data)
        print(gauge_metric)
        terminate = False
        # Update the gauge metric value
        while not terminate:
            # gauge_metric.set(value)  # Update the value
            # push_to_gateway('localhost:8002', job='test_job', registry=registry)

            time.sleep(1000000)
        return "Successfully created prometheus server on port 8002"
    except Exception as e:
        print(str(e))


print(test_push_to_gateway(100000))
