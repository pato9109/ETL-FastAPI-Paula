from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Esta línea crea el "formulario" de login en la página azul que ya viste
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verificar_usuario(token: str = Depends(oauth2_scheme)):
    # Aquí simulamos una validación de seguridad
    if token != "paula123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"usuario": "Paula Admin"}