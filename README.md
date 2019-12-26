# pcd

## Introduction

`pcd` means `powerful cd`, `programmable cd` or `python cd`.

It enables users to create path shortcut or alias in a programmable way.

## Prerequisites

Python >= 3.4

## Start

Run `python3 setup.py`.

Then you can try `python3 pcd.py`.

You can write your customized path function in `function.py`

## Common settings

### PowerShell

Add to your PowerShell profile

``` powershell
$pcd_dir = "D:\pcd"

function pcd
{
    $pcd_out = python "$pcd_dir\pcd.py" @Args
    if ($pcd_out -is "String" -and -not $pcd_out.StartsWith("pcd error: "))
    {
        Set-Location $pcd_out
    }
    else
    {
        Write-Output $pcd_out
    }
}

function ecd
{
    python "$pcd_dir\pcd.py" -i -c "explorer /n,{}"
}
```

### Acknowledgement

The author is hired by Microsoft Corporation.
