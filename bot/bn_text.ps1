# Renders Bengali (or any) text to white-on-black PNG masks using Windows' own text engine,
# which shapes Bengali conjuncts correctly. Input: JSON file of [{text, size, path}].
param([string]$JobFile)
Add-Type -AssemblyName System.Drawing, System.Windows.Forms
$jobs = Get-Content $JobFile -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($j in $jobs) {
    $font = New-Object System.Drawing.Font("Nirmala UI", [float]$j.size, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
    $flags = [System.Windows.Forms.TextFormatFlags]::NoPadding
    $sz = [System.Windows.Forms.TextRenderer]::MeasureText($j.text, $font, (New-Object System.Drawing.Size(4000, 1000)), $flags)
    $bmp = New-Object System.Drawing.Bitmap(($sz.Width + 8), ($sz.Height + 8))
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.Clear([System.Drawing.Color]::Black)
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    [System.Windows.Forms.TextRenderer]::DrawText($g, $j.text, $font, (New-Object System.Drawing.Point(4, 4)), [System.Drawing.Color]::White, $flags)
    $bmp.Save($j.path, [System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose(); $bmp.Dispose(); $font.Dispose()
}
