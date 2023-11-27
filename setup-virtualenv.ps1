# Get and search for Python executable
if (Get-Command "python.exe" -ErrorAction SilentlyContinue) {
    Set-Variable -name Python -value python.exe
} elseif (Get-Command "python3.exe" -ErrorAction SilentlyContinue) {
    Set-Variable -name Python -value python3.exe
} else {
    Write-Host "ERROR: Please install Python."
    Exit
}

# Ensure the virtual environemnt exists
if (-not(Test-Path -Path .\venv\)) {
    Invoke-Expression "$Python -m venv venv"
}

# Ensure the virtual environment contains all packages from requirements.txt
.\venv\Scripts\pip --disable-pip-version-check install wheel
.\venv\Scripts\pip --disable-pip-version-check install -r requirements.txt
