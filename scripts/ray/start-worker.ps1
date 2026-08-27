param(
    [Parameter(Mandatory=$true)][string]$HeadAddress
)

$ErrorActionPreference = 'Stop'
$ray = Join-Path $PSScriptRoot '..\..\.venv\Scripts\ray.exe'
if (-not (Test-Path $ray)) { throw 'Ray executable not found. Run scripts/windows/bootstrap.ps1 first.' }

& $ray stop --force
& $ray start --address=$HeadAddress
