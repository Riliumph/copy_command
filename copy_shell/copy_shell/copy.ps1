#
# Script.ps1
#

Param( [string]$copy_list, [string]$destination)
Write-Debug "copy_list: $copy_list"
Write-Debug "destination: $destination"

Get-Date -Format '[yyyy/MM/dd HH:mm:ss]'
$file_list = New-Object 'System.Collections.Generic.List[System.IO.FileInfo]'
foreach( $line in (Get-Content -Path $copy_list -Encoding UTF8) -as [string[]] ){
	$file = New-Object 'System.IO.FileInfo' ($line)
	$file_list.Add($file)
}

#Get-Date -Format '[yyyy/MM/dd HH:mm:ss] Check destination'
#if ( -not (Test-Path $destination) ){
#    New-Item $destination -type directory
#}


