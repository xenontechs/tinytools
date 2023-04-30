$nowplaying = "c:\nowplaying.txt"
$newplaying = "c:\newplaying.txt"
$appname = "obsidian"

while($true){
    $app = (Get-Process | where {$_.mainWindowTItle -and $_.name -eq $appname})
    $app.MainWindowTitle | Format-Table -HideTableHeaders | out-file $newplaying -Encoding ascii -NoNewline

    if(Compare-Object -ReferenceObject $(Get-Content $nowplaying) -DifferenceObject $(Get-Content $newplaying)){
        Get-Process | where {$_.mainWindowTItle -and $_.name -eq $appname} | select -Property mainWindowTitle | Format-Table -HideTableHeaders | out-file $nowplaying -Encoding ascii -NoNewline
        # Write-Host "diff title"
        }
        else{
            # Write-Host "same title"
            }
    Start-Sleep -Seconds 1
}
