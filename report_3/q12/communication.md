## Issue

**标题**：`--name` 传入空白字符串时程序未报错，仍输出问候语并以 0 退出

**环境**：Debian Linux，Python 3.13，greetlab 包 v0.1.0  
（若涉及 Windows 请待确认）

**复现命令**：
```bash
sdt-greet --name "   "
```


**期望结果**：程序应报参数错误，以非零退出码（如 2）终止。

实际结果：程序输出 Hello, !（含空格），并以退出码 0 正常结束。

待确认：其他空白字符（如 \t、\n）及 Windows 平台的行为是否一致。

提交信息
标题：fix: 校验 --name 参数为空白时以 SystemExit(2) 退出

正文：

问题：空字符串或纯空白字符串未被校验，程序仍输出问候语并以 0 退出，不符合 CLI 工具的错误处理约定。

解决方案：在 cli.py 的 main() 中添加检查，若 name.strip() 为空则调用 sys.exit(2)。

评审意见
类型：Blocking

具体行为：当 --name 为 " " 时，程序输出 Hello, ! 并以 0 退出，未按预期报错。

风险：下游脚本依赖退出码判断执行结果，会误认为调用成功，可能导致逻辑错误或数据污染。

建议动作：在 main() 中增加空白参数校验，无效输入时调用 sys.exit(2) 退出，并更新相关测试。

text

---

### 📂 操作步骤（如果还没做）

```bash
cd ~/expriment_reports/report_3/q11   # 确保在 q11 目录
nano communication.md                 # 创建并编辑文件
# 粘贴上面全部内容，Ctrl+O 保存，Ctrl+X 退出
cat communication.md                  # 确认内容已写入
