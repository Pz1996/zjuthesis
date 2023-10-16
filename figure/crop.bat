@echo off

REM 遍历文件夹中的所有pdf文件
for %%i in (*.pdf) do (
    REM 执行pdfcrop操作，并覆盖原文件
    pdfcrop.exe -- %%i %%i
)

echo 所有PDF已经裁剪完成。