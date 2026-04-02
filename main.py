# ==============================================
# 成语接龙（RAG版）后端服务
# 功能：AI自玩、玩家VS AI、玩家出题AI对
# ==============================================
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import random
import uvicorn

app = FastAPI()

# 挂载静态文件（HTML界面）
app.mount("/static", StaticFiles(directory="static"), name="static")

# ----------------------
# 加载成语库
# ----------------------
def load_idioms():
    try:
        with open("idioms.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"加载成语库失败: {e}")
        return ["一帆风顺", "顺理成章", "柳暗花明", "明察秋毫", "毫厘不爽"]

IDIOMS = load_idioms()

# ----------------------
# 工具函数
# ----------------------
def random_start():
    return random.choice(IDIOMS)

def valid_next(current):
    last_char = current[-1]
    return [idiom for idiom in IDIOMS if idiom.startswith(last_char) and idiom != current]

def check_valid(idiom, current):
    return idiom in IDIOMS and idiom.startswith(current[-1])

# ----------------------
# 路由：首页
# ----------------------
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

# ----------------------
# 接口1：AI自动接龙
# ----------------------
@app.get("/api/ai_auto_play")
async def ai_auto_play(start: str = None, rounds: int = 10):
    if not start or start not in IDIOMS:
        start = random_start()
    result = [start]
    current = start
    for _ in range(rounds - 1):
        candidates = valid_next(current)
        if not candidates:
            break
        next_idiom = random.choice(candidates)
        result.append(next_idiom)
        current = next_idiom
    return {"start": start, "result": result}

# ----------------------
# 接口2：AI接玩家的成语（玩家出题AI对）
# ----------------------
@app.get("/api/ai_reply")
async def ai_reply(user_idiom: str):
    if user_idiom not in IDIOMS:
        return {"status": "error", "message": "成语不在文档中！"}
    candidates = valid_next(user_idiom)
    if not candidates:
        return {"status": "success", "ai_idiom": None, "message": "AI没有可接的成语，你赢了！"}
    ai_idiom = random.choice(candidates)
    return {"status": "success", "ai_idiom": ai_idiom}

# ----------------------
# 接口3：玩家VS AI对战校验
# ----------------------
@app.get("/api/vs_check")
async def vs_check(user_idiom: str, current_idiom: str):
    if user_idiom not in IDIOMS:
        return {"status": "error", "message": "成语不在文档中，你输了！"}
    if not user_idiom.startswith(current_idiom[-1]):
        return {"status": "error", "message": f"需要以【{current_idiom[-1]}】开头，你输了！"}
    # AI接龙
    candidates = valid_next(user_idiom)
    if not candidates:
        return {"status": "success", "ai_idiom": None, "message": "AI没有可接的成语，你赢了！"}
    ai_idiom = random.choice(candidates)
    return {"status": "success", "user_idiom": user_idiom, "ai_idiom": ai_idiom}

# ----------------------
# 接口4：获取随机起始成语
# ----------------------
@app.get("/api/random_start")
async def get_random_start():
    return {"start": random_start()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)