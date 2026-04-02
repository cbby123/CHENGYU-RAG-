markdown
# 成语接龙（RAG版）
## 📌 课堂独立项目
基于 **FastAPI + HTML前端 + 成语文档检索** 实现的成语接龙游戏，支持网页界面操作。

## ✨ 功能特性
- 🎨 **美观网页界面**：浏览器打开即可玩，替代命令行
- 🤖 **AI自动接龙**：AI随机开头，连续接龙10轮
- 🎮 **玩家VS AI对战**：玩家输入成语，AI回应，违规判负
- 📝 **玩家出题AI对**：玩家出成语，AI自动接龙
- ✅ **严格文档校验**：所有成语必须来自`idioms.txt`，否则判负
- 🔄 **随机开头**：每次游戏不重复

## 🚀 快速启动
### 1. 安装依赖
```bash
pip install fastapi uvicorn
2. 启动服务
bash
运行
python main.py
3. 打开浏览器
访问 http://localhost:8000 即可进入游戏界面
📁 项目结构
plaintext
CHENGYU-RAG/
├── main.py              # FastAPI后端服务
├── idioms.txt           # 成语库（120+常用成语）
├── static/
│   └── index.html       # 前端HTML界面
└── README.md
🎮 游戏模式说明
1. AI 自动接龙
点击「开始 AI 自动接龙」，AI 会随机选择起始成语，连续接龙 10 轮，全程自动运行。
2. 玩家 VS AI 对战
点击「开始对战」，AI 随机出起始成语，玩家输入成语接龙，AI 回应，违规（不在文档 / 接错）判负。
3. 玩家出题 AI 对
玩家输入任意成语，AI 自动接龙，支持玩家出题考验 AI。
