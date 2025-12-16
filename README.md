## Healthcheck / Auto-restart
The app container is configured with a Docker healthcheck against `/health` and `restart: unless-stopped`.

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
