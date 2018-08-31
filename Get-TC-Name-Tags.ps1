$files = Get-ChildItem *.xml

$azure_only = 0
$hyperv_only = 0
$both_platforms = 0
$tags = @{}

foreach ($fname in $files) {
    $xml = [xml](Get-Content $fname)
    foreach ($item in $xml.TestCases.test) {
        Write-host $item.testName, $item.Platform, $item.Category, $item.Area, $item.Tags 
        
        if ($item.Platform -eq "HyperV") {
            $hyperv_only++
        } elseif ($item.Platform -eq "Azure") {
            $azure_only++
        } else {
            $both_platforms++
        }
        foreach ($single_tag in $item.Tags.Split(",")) {
            if ($tags.ContainsKey($single_tag)) {
                $tags[$single_tag]++
            } else {
                $tags.Add($single_tag, 1)
            }

        }
    }
}
Write-Host ""
Write-Host "Azure only: $azure_only"
Write-Host "Hyper-V only: $hyperv_only"
Write-Host "Both platforms: $both_platforms"
Write-Host ""

$tags
