Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -Name EnableScriptBlockLogging -Value 1 -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\Transcription" -Name EnableTranscripting -Value 1 -Force
https://github.com/SwiftOnSecurity/sysmon-config/blob/master/sysmonconfig-export.xml
