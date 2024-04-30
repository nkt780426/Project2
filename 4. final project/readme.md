Get-NetIPAddress | Where-Object {$_.AddressFamily -eq "IPv4" -and $_.PrefixLength -eq "24"} | Select-Object -ExpandProperty IPAddress

Nhược điểm: 
- Cười đau mặt mới tính là cười :))