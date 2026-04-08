param(
  [string]$RepoUrl = "https://github.com/killerkain/BTC-KRW-anal.git",
  [string]$Branch = "main"
)
$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  if (Get-Command winget -ErrorAction SilentlyContinue) {
    winget install --id Git.Git -e --source winget
  } else {
    throw "git이 없습니다. https://git-scm.com/download/win 에서 먼저 설치하세요."
  }
}

if (-not (Test-Path ".git")) { git init }
git add -A
git commit -m "initial upload" 2>$null

$remoteExists = (git remote 2>$null | Select-String "^origin$" -Quiet)
if ($remoteExists) { git remote set-url origin $RepoUrl } else { git remote add origin $RepoUrl }

git branch -M $Branch
git push -u origin $Branch
