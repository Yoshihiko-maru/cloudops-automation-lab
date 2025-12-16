# cloudops-automation-lab
A small but production-minded lab project to demonstrate:
- IaC mindset (reproducible setup)
- Observability (Prometheus / Grafana)
- Alerting pipeline (Prometheus rules -> Alertmanager)
- Incident operation (Runbook + Postmortem)
- Preventative hardening (healthcheck + auto-restart)

## Quick Start
```powershell
docker compose up -d --build
<<<<<<< HEAD
Validation:
- `docker ps` shows `cloudops_app` as `(healthy)`

## Evidence (Screenshots)

### ServiceDown: Pending → Firing → Resolved
![Prometheus Pending](docs/screenshots/pending.png)
![Prometheus Firing](docs/screenshots/firing.png)
![Alertmanager Firing](docs/screenshots/alert_manager.png)
![Alertmanager Resolved](docs/screenshots/resolved_manager.png)

### Healthcheck
![docker ps healthy](docs/screenshots/docker_healthy.png)
=======

>>>>>>> f5b6814d338488df88771595929186f16f8fe3a9
