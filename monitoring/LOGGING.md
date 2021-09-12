# Logging

This repository uses stack of following tools: grafana, promtail, loki.

## Best practices (docker-compose)

 * Use custom networks in docker-compose for splitting areas of work and inproves names for logging.
 * Use descriptive names for services in docker-compose.
 * Use global parts in names in docker-compose for better logging with multiple containers.

## Best practices (logging)

 * Graphs sholud simplify perception.
 * Use tags/names for splitting logs from different sources.

## Screenshots

 * Grafana
![Grafana](https://github.com/bogotolec/devops/blob/master/monitoring/screenshots/grafana.png)
 * Loki
![Loki](https://github.com/bogotolec/devops/blob/master/monitoring/screenshots/loki.png)
 * Loki dashboard
![Loki](https://github.com/bogotolec/devops/blob/master/monitoring/screenshots/loki_dashboard.png)
 * Prometheus in Grafana
![Prometheus](https://github.com/bogotolec/devops/blob/master/monitoring/screenshots/prometheus.png)
 * Prometheus interface
![Prometheus](https://github.com/bogotolec/devops/blob/master/monitoring/screenshots/prometheus_interface.png)
 * Prometheus dashboard
![Prometheus](https://github.com/bogotolec/devops/blob/master/monitoring/screenshots/prometheus_dashboard.png)
