## Healthcheck / Auto-restart
The app container is configured with a Docker healthcheck against `/health` and `restart: unless-stopped`.

Validation:
- `docker ps` shows `cloudops_app` as `(healthy)`
