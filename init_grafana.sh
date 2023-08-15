prometheus_dir="~/PycharmProjects/prometheus-2.45.0.linux-amd64"

## RUN PROMETHEUS CLIENT
python3 Prometheus-Client/cost.py > prometheus_client.log 2>&1 &
echo "prometheus client running on port 8002"


# RUN PROMETHEUS SERVER
# By default prometheus server runs on port 9090

sudo ~/PycharmProjects/prometheus-2.45.0.linux-amd64/prometheus > prometheus_server.log 2>&1 &
echo " prometheus running on http://localhost:9090"

# RUN GRAFANA IF NOT RUNNING
systemctl start grafana-server
echo "grafana running on port 3000"