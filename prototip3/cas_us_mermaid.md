# Diagrama de Casos de Uso

```mermaid
graph TD
    %% Definición de Actores
    T[Tutor / Cuidador]
    A[Administrador]

    %% Definición de Casos de Uso (Burbujas)
    UC1((Autenticarse - Login))
    UC2((Visualizar Childs))

    %% Relaciones
    T --- UC1
    T --- UC2
    A --- UC1
    A --- UC2

    %% Estilo para que parezcan casos de uso
    style UC1 fill:#f9f,stroke:#333,stroke-width:2px
    style UC2 fill:#bbf,stroke:#333,stroke-width:2px
    