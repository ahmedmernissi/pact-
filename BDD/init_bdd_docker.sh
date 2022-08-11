# Create bdd server
echo "[*] Creating the server ..."
docker run --rm -d -p 5432:5432 -e POSTGRES_PASSWORD=PACT25 --name postgres postgres

echo "[*] Waiting for server to be up and running ..."
sleep 30
echo "[*] Init database on the server ..."

# Create database in postgres
docker exec postgres psql -U postgres -c "CREATE DATABASE sens_art;"
