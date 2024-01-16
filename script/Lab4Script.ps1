# Configuration Script for Hardening
# Ensure execution policy allows script to run
Set-ExecutionPolicy Bypass -Force -Scope Process

# Function to configure 1.1.5 (L1): Ensure 'Password must meet complexity requirements' is set to 'Enabled'
Function ConfigurePasswordComplexity {
    Write-Host "Configuring Password Complexity..."
    # Enable Password Complexity
    secedit /export /cfg C:\secpol.cfg
    (Get-Content C:\secpol.cfg).Replace("PasswordComplexity = 0", "PasswordComplexity = 1") | Set-Content C:\secpol.cfg
    secedit /configure /db %windir%\security\new.sdb /cfg C:\secpol.cfg /areas SECURITYPOLICY
    gpupdate /force
    Write-Host "Password Complexity Configured."
}

# Function to configure 18.4.3 (L1): Ensure 'Configure SMB v1 client driver' is set to 'Enabled: Disable driver (recommended)'
Function ConfigureSMBv1ClientDriver {
    Write-Host "Configuring SMBv1 Client Driver..."
    # Disable SMBv1 Client Driver
    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\mrxsmb10" -Name "Start" -Value 4
    Write-Host "SMBv1 Client Driver Configured."
}

# Main Script
try {
    # Run functions to configure settings
    ConfigurePasswordComplexity
    ConfigureSMBv1ClientDriver

    Write-Host "Configuration Completed Successfully."
} catch {
    Write-Host "An error occurred: $_"
}
