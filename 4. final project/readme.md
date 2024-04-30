https://learn.microsoft.com/en-us/windows/wsl/connect-usb
https://github.com/phuoctan4141/WSL/blob/main/Connect%20USB%20devices/USB%20Camera.md
https://github.com/dorssel/usbipd-win

Get-NetIPAddress | Where-Object {$_.AddressFamily -eq "IPv4" -and $_.PrefixLength -eq "24"} | Select-Object -ExpandProperty IPAddress