# Infrastructure & Observability Lab

A hands-on SRE environment built on **Proxmox VE** featuring a high-performance PostgreSQL database, automated transaction monitoring, and a full Prometheus/Grafana stack.

## 🚀 Architecture
- **Hypervisor:** Proxmox VE
- **Database Node (CT 100):** PostgreSQL 16 on Debian 12
- **Monitoring Node (CT 101):** Prometheus & Grafana
- **Traffic Simulation:** Python 3.11

## 📊 Monitoring Capabilities
- **Host Telemetry:** Node Exporter tracking CPU, RAM, and Disk I/O.
- **DB Insights:** Postgres Exporter tracking transaction throughput, cache hits, and locks.
- **Visualization:** Custom Grafana dashboards for performance correlation.

## 🛠️ How to Run the Load Test
1. Ensure the PostgreSQL container is active.
2. Run the simulation script from the host or client machine:
   ```bash
   python3 scripts/bulk_load.py
