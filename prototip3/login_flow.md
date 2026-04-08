sequenceDiagram
    autonumber
    actor Usuario as Actor (Tutor/Cuidador/Admin)
    participant Servidor as Servidor TapatApp
    participant BBDD as Base de Datos

    Note over Usuario, Servidor: Precondición: El usuario debe estar registrado

    Usuario->>Servidor: Envía username y password
    
    alt Credenciales Válidas (Flujo Principal)
        Servidor->>Servidor: Valida credenciales
        Servidor->>Servidor: Genera un Token
        Servidor->>BBDD: Almacena el Token
        BBDD-->>Servidor: Confirmación de guardado
        Servidor-->>Usuario: Devuelve Token y datos del usuario
        Note right of Usuario: Postcondición: Usuario autenticado
    else Credenciales Incorrectas (Flujo Alternativo)
        Servidor-->>Usuario: Error 401 Unauthorized
    end