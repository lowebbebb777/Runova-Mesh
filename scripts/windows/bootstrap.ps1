$ErrorActionPreference = 'Stop'

if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
    throw 'Python launcher (py) was not found. Install Python 3.11+ first.'
}

if (-not (Test-Path '.venv')) {
    py -m venv .venv
}

& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -e '.[ray,dev]'
& .\.venv\Scripts\runova-mesh.exe probe
