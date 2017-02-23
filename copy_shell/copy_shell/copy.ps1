#
# Script.ps1
#

Param( 
	[parameter(Mandatory=$true)][string]$copy_list,
	[Parameter(Mandatory=$true)][string]$destination
)

Write-Debug "copy_list: $copy_list"
Write-Debug "destination: $destination"

Write-Host ("[{0}] Get file path from list..." -f (Get-Date -Format 'yyyy/MM/dd HH:mm:ss').ToString())
$file_list = New-Object 'System.Collections.Generic.List[System.IO.FileInfo]'
$miss_list = New-Object 'System.Collections.Generic.List[System.IO.FileInfo]'
foreach( $line in (Get-Content -Path $copy_list -Encoding UTF8) -as [string[]] ){
	$file = New-Object 'System.IO.FileInfo' ($line)
	if ( $file.Exists ){
		$file_list.Add($file)
	}else{
		$miss_list.Add($file)
	}
}

Write-Host ("[{0}] Missing file quantity: {1}" -f 
	(Get-Date -Format 'yyyy/MM/dd HH:mm:ss').ToString(),
	$miss_list.Count
)
$miss_list | Set-Content ./miss_list.log -Encoding UTF8

Write-Host ("[{0}] Check destination path..." -f (Get-Date -Format 'yyyy/MM/dd HH:mm:ss').ToString())
if ( -not (Test-Path $destination) ){
	New-Item $destination -type directory | Out-Null
}

foreach( $file in $file_list ){
	Write-Host ("Copying ... {0}" -f $file )
	Copy-Item -LiteralPath $file $destination
}

Write-Host ("[{0}] All is done!!" -f (Get-Date -Format 'yyyy/MM/dd HH:mm:ss').ToString())