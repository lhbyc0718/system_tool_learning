## 核心提示
当 --name 为空白字符串时，程序应以 SystemExit(2) 退出。
## 智能体改动
在 cli.py 的 main() 中添加 if not a.name.strip(): sys.exit(2)。
## 人工验证
pytest tests/ 通过，diff 仅包含上述改动。
