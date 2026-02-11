#!/bin/sh
set -e

# This script runs inside the container (after image build).
# It waits until the DATABASE_URL host accepts connections, then execs the repo entrypoint.
# It relies on psycopg2 being installed in the image (your requirements.txt already includes it).

echo "Waiting for database to be reachable..."

python - <<'PY'
import os, time, sys
import urllib.parse
import psycopg2

url = os.environ.get("DATABASE_URL")
if not url:
    print("DATABASE_URL not set")
    sys.exit(1)

parts = urllib.parse.urlparse(url)
host = parts.hostname or "localhost"
port = parts.port or 5432
user = parts.username or ""
password = parts.password or ""
dbname = parts.path.lstrip("/")

for attempt in range(60):
    try:
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=dbname, connect_timeout=3)
        conn.close()
        print("Database reachable")
        sys.exit(0)
    except Exception as e:
        time.sleep(1)
print("Database not reachable after 60s", file=sys.stderr)
sys.exit(1)
PY

echo "Starting application entrypoint..."
exec ./entrypoint.sh
