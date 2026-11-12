# Toutes les query utilent:

Pourcetage de CPU utilisé:
`100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)`

Pourcentage de la mémoire utilisée:
`100 - ((node_memory_MemAvailable_bytes * 100) / node_memory_MemTotal_bytes)`

Pourcentage d'espace disque utilisé:
`100 - ((node_filesystem_avail_bytes{mountpoint=~"/.*"} * 100) / node_filesystem_size_bytes{mountpoint=~"/.*"})`

Débit réseau entrant en octets/s :
`rate(node_network_receive_bytes_total{device!="lo"}[5m])`

p95 de latence:
`histogram_quantile(0.95, sum by (le, handler) (rate(prometheus_http_request_duration_seconds_bucket[5m])))`