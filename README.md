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


========================================================
FASTAPI + DOCKER DEVELOPMENT WORKFLOW
========================================================

1. ADD / MODIFY / REMOVE AN API
--------------------------------------------------------
Change your Python files normally.

Example:
app/routes/user_routes.py
app/controllers/user_controller.py
app/services/user_service.py

Then:

docker compose restart api

OR, if the API container needs to be recreated:

docker compose up -d api


--------------------------------------------------------
2. INSTALL A NEW PYTHON PACKAGE
--------------------------------------------------------
Example:

pip install passlib
pip install argon2-cffi

IMPORTANT:
Do NOT rely only on installing it locally.

Add the package to:

requirements.txt

Example:

fastapi
uvicorn[standard]
sqlalchemy
psycopg
python-dotenv
alembic
passlib
argon2-cffi
python-jose
email-validator
pydantic-settings


Then rebuild the Docker image:

docker compose down

docker compose build --no-cache

docker compose up -d


OR simply:

docker compose up -d --build


Use --build whenever requirements.txt changes.


--------------------------------------------------------
3. REMOVE A PYTHON PACKAGE
--------------------------------------------------------
Remove it from:

requirements.txt

Then rebuild:

docker compose down

docker compose build --no-cache

docker compose up -d


--------------------------------------------------------
4. ONLY PYTHON CODE CHANGED
--------------------------------------------------------
If your docker-compose.yml has a volume like:

./app:/app/app

then usually you don't need to rebuild.

Just:

docker compose restart api


If there is NO volume mount:

docker compose up -d --build api


--------------------------------------------------------
5. DATABASE CODE / SQLALCHEMY MODEL CHANGED
--------------------------------------------------------
If you changed a model:

app/models/user.py

Create migration:

docker compose exec api alembic revision --autogenerate -m "describe change"

Then:

docker compose exec api alembic upgrade head


Then restart API if needed:

docker compose restart api


--------------------------------------------------------
6. .env CHANGED
--------------------------------------------------------
After changing environment variables:

docker compose up -d --force-recreate api


If DATABASE_URL changed, recreate the API container.


--------------------------------------------------------
7. docker-compose.yml CHANGED
--------------------------------------------------------
Example:
ports
environment
volumes
depends_on
database configuration

Run:

docker compose down

docker compose up -d --build


--------------------------------------------------------
8. Dockerfile CHANGED
--------------------------------------------------------
Run:

docker compose up -d --build


For a completely clean rebuild:

docker compose down

docker compose build --no-cache

docker compose up -d


--------------------------------------------------------
9. CHECK CONTAINERS
--------------------------------------------------------
docker compose ps


You want:

fastapi_app    Up
postgres_db    Up (healthy)


--------------------------------------------------------
10. CHECK API LOGS
--------------------------------------------------------
docker compose logs api --tail=100


Live logs:

docker compose logs -f api


Database logs:

docker compose logs -f db


--------------------------------------------------------
11. CHECK DATABASE
--------------------------------------------------------
docker exec -it postgres_db psql -U postgres -l


Connect to your database:

docker exec -it postgres_db psql -U postgres -d fastapi_db


--------------------------------------------------------
12. TEST API
--------------------------------------------------------
Open:

http://localhost:8000/docs


Or:

http://localhost:8000


--------------------------------------------------------
13. STOP EVERYTHING
--------------------------------------------------------
docker compose stop


This stops containers but keeps them.


--------------------------------------------------------
14. START EVERYTHING AGAIN
--------------------------------------------------------
docker compose start


--------------------------------------------------------
15. NORMAL RESTART
--------------------------------------------------------
docker compose restart


Only restart containers.


--------------------------------------------------------
16. RECREATE EVERYTHING
--------------------------------------------------------
docker compose down

docker compose up -d --build


--------------------------------------------------------
17. COMPLETE CLEAN RESET
--------------------------------------------------------
WARNING:
This removes the PostgreSQL Docker volume and therefore
deletes the database data stored in that Docker volume.

docker compose down -v

docker compose up -d --build


DO NOT use this casually.


========================================================
GITHUB WORKFLOW
========================================================

After code changes:

git status

git add .

git commit -m "Add user API"

git push


Before pushing, make sure:

.env

is NOT committed.


Your .gitignore should contain:

.env
__pycache__/
*.pyc
.venv/
venv/
.idea/
.vscode/


========================================================
QUICK DECISION TABLE
========================================================

Changed Python/API code
        ↓
docker compose restart api

Changed requirements.txt
        ↓
docker compose up -d --build

Added/removed Python package
        ↓
Update requirements.txt
        ↓
docker compose up -d --build

Changed Dockerfile
        ↓
docker compose up -d --build

Changed docker-compose.yml
        ↓
docker compose down
docker compose up -d --build

Changed .env
        ↓
docker compose up -d --force-recreate api

Changed SQLAlchemy model
        ↓
alembic revision --autogenerate
        ↓
alembic upgrade head

Need to stop containers
        ↓
docker compose stop

Need to start them again
        ↓
docker compose start

Need to completely recreate containers
        ↓
docker compose down
docker compose up -d --build

Need to delete database volume
        ↓
docker compose down -v
        ↓
⚠️ DATABASE DATA IS DELETED
========================================================