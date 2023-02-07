from fastapi import HTTPException, status

credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

inactive_user = HTTPException(status_code=400, detail="Usuario Inactivo")

incorrect_user = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="email o password Incorrecto",
                headers={"WWW-Authenticate": "Bearer"},
            )