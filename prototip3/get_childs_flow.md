sequenceDiagram
    autonumber
    actor Usuario as Actor Autenticado
    participant Servidor as Servidor TapatApp
    participant BBDD as Base de Datos

    Note over Usuario, Servidor: Acceso a recurso protegido (Childs)

    Usuario->>Servidor: Solicita lista de Childs + Token
    
    Servidor->>BBDD: Valida Token y permisos del usuario
    
    alt Token Válido y Autorizado
        BBDD-->>Servidor: Retorna datos de los Childs
        Servidor-->>Usuario: Envía JSON con Childs (200 OK)
    else Token Inválido o Expirado
        Servidor-->>Usuario: Error 401 Unauthorized / 403 Forbidden
    end