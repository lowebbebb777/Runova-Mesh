param(
    [string]$NodeIp = '127.0.0.1',
    [int]$Port = 6379
)

$ErrorActionPreference = 'Stop'
$ray = Join-Path $PSScriptRoot '..\..\.venv\Scripts\ray.exe'
if (-not (Test-Path $ray)) { throw 'Ray executable not found. Run scripts/windows/bootstrap.ps1 first.' }

& $ray stop --force
& $ray start --head --node-ip-address=$NodeIp --port=$Port
