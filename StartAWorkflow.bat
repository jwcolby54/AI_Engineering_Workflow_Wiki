@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "BOOTSTRAP=%SCRIPT_DIR%skills\start-ai-engineering-workflow\scripts\workflow_bootstrap.py"

python "%BOOTSTRAP%" %*

endlocal
