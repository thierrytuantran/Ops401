# PowerShell script to configure automatic screen lock settings

# Define the registry key paths
$screenSaverKeyPath = "HKCU:\Control Panel\Desktop"
$screenSaverValueName = "ScreenSaveActive"
$screenSaverTimeoutValueName = "ScreenSaveTimeOut"

# Set screen lock parameters
$screenLockEnabled = 1  # 1 to enable screen lock, 0 to disable
$screenLockTimeoutSeconds = 900  # Set the timeout value in seconds (15 minutes in this example)

# Update registry values to enable screen lock and set timeout
Set-ItemProperty -Path $screenSaverKeyPath -Name $screenSaverValueName -Value $screenLockEnabled
Set-ItemProperty -Path $screenSaverKeyPath -Name $screenSaverTimeoutValueName -Value $screenLockTimeoutSeconds

# Output success message
Write-Host "Automatic screen lock configuration completed successfully."
