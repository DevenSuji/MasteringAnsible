[CmdletBinding()]
param (
    [Parameter(Mandatory)]
    [String]$ComputerName
)

Invoke-Command -ComputerName $ComputerName -ScriptBlock {
    $Installer = "$env:temp\chrome_installer.exe"
    $url = 'http://dl.google.com/chrome/install/375.126/chrome_installer.exe'
    Invoke-WebRequest -Uri $url -OutFile $Installer -UseBasicParsing
    Start-Process -FilePath $Installer -Args '/silent /install' -Wait
    Remove-Item -Path $Installer

    $IsGoogleChromeInstalled = (Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo

    if ($Null -eq $IsGoogleChromeInstalled.FileName) {
        Write-Output "Chrome Installation Failed"
    }
    else {
        Write-Output "Chrome Install Successfully"
    }
}


