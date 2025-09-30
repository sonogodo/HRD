from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/match_vaga")
async def match_vaga(descricao: str = Form(...)):
    # Dummy response for demonstration
    return {"mensagem": "Vaga recebida com sucesso!", "descricao_recebida": descricao}

@app.post("/match_vagas")
async def match_vagas(file: UploadFile = File(...)):
    # Dummy response for demonstration
    content = await file.read()
    try:
        # Try to decode JSON file
        import json
        data = json.loads(content.decode("utf-8"))
        return {"mensagem": "Arquivo recebido com sucesso!", "dados_recebidos": data}
    except Exception as e:
        return JSONResponse(status_code=400, content={"erro": "Arquivo inválido ou não é um JSON.", "detalhes": str(e)})

@app.get("/")
async def root():
    return {"mensagem": "API FastAPI está funcionando!"}

# For Vercel compatibility
handler = app