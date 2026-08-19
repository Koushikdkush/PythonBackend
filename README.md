"# PythonBackend" 
# PythonBackend

<!-- commands to for alembic migration -->
#production level migration 
#python -m alembic revision --autogenerate -m "describe change"
#python -m alembic upgrade head

<!-- Command to start server -->
#python -m uvicorn app.main:app --reload

[//]: # (docker compose up -d --build api)

# 1. Start
docker compose up -d

# 2. Start + rebuild
docker compose up -d --build

# 3. Rebuild API only
docker compose up -d --build api

# 4. Restart
docker compose restart

# 5. Restart API
docker compose restart api

# 6. Stop/remove containers
docker compose down

# 7. Check status
docker compose ps

# 8. API logs
docker compose logs api --tail=100

# 9. PostgreSQL logs
docker compose logs db --tail=100

# 10. Open PostgreSQL
docker exec -it postgres_db psql -U postgres