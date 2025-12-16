import os
import time
import logging
from typing import Optional

from fastapi import FastAPI, Response
from pythonjsonlogger import jsonlogger
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

APP_NAME = os.getenv("APP_NAME", "cloudops-automation-lab")

# Logging: JSON to stdout
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
logger.addHandler(handler)

# Prometheus metrics
REQ_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status"],
)
REQ_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency in seconds",
    ["path"],
    buckets=(0.05, 0.1, 0.2, 0.3, 0.5, 1, 2, 5),
)

app = FastAPI(title=APP_NAME)


@app.middleware("http")
async def metrics_middleware(request, call_next):
    start = time.time()
    status = 500
    try:
        resp = await call_next(request)
        status = resp.status_code
        return resp
    finally:
        elapsed = time.time() - start
        path = request.url.path
        REQ_LATENCY.labels(path=path).observe(elapsed)
        REQ_COUNT.labels(method=request.method, path=path, status=str(status)).inc()
        logger.info("request", extra={"path": path, "method": request.method, "status": status, "latency_s": elapsed})


@app.get("/health")
def health():
    return {"status": "ok", "service": APP_NAME}


@app.get("/error")
def error():
    logger.error("intentional_error", extra={"reason": "demo"})
    return Response(content="intentional error", status_code=500)


@app.get("/latency")
def latency(ms: Optional[int] = 0):
    ms = max(0, min(int(ms or 0), 10_000))
    time.sleep(ms / 1000.0)
    return {"slept_ms": ms}


@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)
