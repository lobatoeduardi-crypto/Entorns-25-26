# Diagrama de Secuencia: LOGIN

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant Servidor
    participant BBDD

    Usuario->>Servidor: Envía username y password
    
    Note over Servidor: El servidor valida los datos
    
    alt Credenciales Correctas
        Servidor->>Servidor: Genera Token
        Servidor->>BBDD: Guarda Token
        Servidor-->>Usuario: Devuelve Token y Datos (200 OK)
    else Credenciales Incorrectas
        Servidor-->>Usuario: Error 401 Unauthorized
    end