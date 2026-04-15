# Diagrama de Casos de Uso (TapatApp)

```mermaid
graph LR
    %% Actores
    T((Tutor / Cuidador))
    A((Administrador))

    %% Caja del Sistema
    subgraph Sistema_TapatApp [Sistema TapatApp - Prototip 3]
        UC1([CU-01: Login])
        UC2([CU-02: ViewChild])
    end

    %% Conexiones
    T --- UC1
    T --- UC2
    
    A --- UC1
    A --- UC2

    %% Estilos para que parezcan óvalos de casos de uso
    style UC1 fill:#ffffff,stroke:#333,stroke-width:2px
    style UC2 fill:#ffffff,stroke:#333,stroke-width:2px
    style Sistema_TapatApp fill:#f9f9f9,stroke:#666,stroke-dasharray: 5 5
    