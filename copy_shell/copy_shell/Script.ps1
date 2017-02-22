#
# Script.ps1
#
Param( [string]$copy_list='./input.txt', [string]$destination='dest')
Write-Debug "copy_list: $copy_list"
Write-Debug "destination: $destination"

Get-Date -Format '[yyyy/MM/dd HH:mm:ss]'
$path_list = New-Object 'System.Collections.Generic.List[System.IO.Path]'
foreach( $line in Get-Content $copy_list){
    $path = New-Object 'System.IO.Path' ($line)
    $path_list.Add($file)
}

foreach( $path in $path_list){
    Write-Output $path
}

#Get-Date -Format '[yyyy/MM/dd HH:mm:ss] Check destination'
#if ( -not (Test-Path $destination) ){
#    New-Item $destination -type directory
#}


