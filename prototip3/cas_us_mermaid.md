# Diagrama de Casos de Uso

```mermaid
usecaseDiagram
    actor "Tutor/Cuidador" as u
    actor "Administrador" as admin
    
    package "TapatApp - Prototipo 3" {
        usecase "Autenticarse (Login)" as UC_Login
        usecase "Visualizar Childs" as UC_ViewChilds
    }

    u --> UC_Login
    u --> UC_ViewChilds
    admin --> UC_Login
    admin --> UC_ViewChilds
    