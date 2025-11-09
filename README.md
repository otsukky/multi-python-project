# MULTI-PYTHON-PROJECT

## 概要

uvを使ったモノレポ構成お試しリポジトリ

## 初期化過程

1. `mkdir フォルダ名 | cd フォルダ名`
2. `uv init -p pythonバージョン --no-readme`
3. `uv add ruff===0.14.4`
4. `touch .gitignore`
5. 作成したフォルダ内のpyproject.tomlに共通のruff設定を通す
```toml
[tool.ruff]
extend = "../config/ruff.toml"
```
6. `mkdir フォルダ名/.vscode | touch フォルダ名/.vscode/settings.json`
