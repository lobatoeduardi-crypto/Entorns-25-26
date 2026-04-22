# [CU-02] Visualizar Childs

| Campo | Detalle |
| :--- | :--- |
| **Descripción** | El usuario autenticado solicita ver la lista de niños a su cargo. |
| **Actores** | Tutor, Cuidador, Administrador |
| **Precondiciones** | El usuario debe tener un token de sesión válido (estar logueado). |
| **Postcondiciones** | Se muestra en pantalla la información detallada de los niños asociados. |

### Secuencia Normal
| # | Acción (actor) | Reacción (sistema) |
| :--- | :--- | :--- |
| 1 | El usuario pulsa en "Ver lista de niños". | El sistema envía petición GET con el Token en el header. |
| 2 | | El servidor valida el token y busca los datos en la BBDD. |
| 3 | | El sistema recibe el JSON con los datos y los renderiza en la vista. |

### Excepciones
| # | Acción (actor) | Reacción (sistema) |
| :--- | :--- | :--- |
| p | El token ha expirado. | El sistema devuelve error **403 Forbidden** y redirige al Login. |

### Otros Datos
| Campo | Detalle |
| :--- | :--- |
| **Rendimiento** | La carga de la lista no debe superar los 3 segundos. |
| **Frecuencia** | Se espera una media de 10 veces al día por usuario. |
| **Importancia** | Importante |
| **Urgencia** | Hay presión |
| **Comentarios** | Los datos mostrados dependen estrictamente de los permisos del usuario. |
