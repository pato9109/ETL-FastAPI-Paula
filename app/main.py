from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import verificar_usuario
from app.etl_process import procesar_y_guardar_ventas

app = FastAPI()

# --- ESTA ES LA RUTA QUE TE FALTA PARA EL BOTÓN VERDE ---
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Aquí validamos la "llave" que pusimos antes
    if form_data.password == "paula123":
        return {"access_token": "paula123", "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Contraseña incorrecta")

@app.get("/")
def inicio():
    return {"mensaje": "Pipeline ETL de Paula funcionando"}

@app.get("/datos-ventas")
def obtener_datos(usuario: dict = Depends(verificar_usuario)):
    # Ejecuta el proceso ETL y guarda en SQL
    datos = procesar_y_guardar_ventas()
    return {"ejecutado_por": usuario["usuario"], "resultado": datos}