param (
    [string]$envType = "local"
)

if ($envType -eq "docker") {
    $env:DB_HOST="db"
} else {
    $env:DB_HOST="localhost"
}

$env:POSTGRES_DB="chatapp"
$env:POSTGRES_USER="postgres"
$env:POSTGRES_PASSWORD="postgres"
$env:DB_PORT="5432"
$env:SECRET_KEY="your-secret-key"
$env:REDIS_HOST="127.0.0.1"
$env:REDIS_PORT="6379"

Write-Host "Environment variables set for $envType environment successfully."
