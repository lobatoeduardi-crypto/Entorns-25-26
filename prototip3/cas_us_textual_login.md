# [CU-01] Autenticación de Usuario (Login)

| Campo | Detalle |
| :--- | :--- |
| **Descripción** | El usuario introduce sus credenciales para obtener acceso al sistema y un token de seguridad. |
| **Actores** | Tutor, Cuidador, Administrador |
| **Precondiciones** | El usuario debe estar registrado previamente en la base de datos. |
| **Postcondiciones** | El usuario queda autenticado y el sistema genera un token de sesión válido. |

### Secuencia Normal
| # | Acción (actor) | Reacción (sistema) |
| :--- | :--- | :--- |
| 1 | El usuario introduce `username` y `password`. | El sistema recibe los datos y los envía al servidor. |
| 2 | | El servidor valida las credenciales contra la BBDD. |
| 3 | | El servidor genera un token y lo almacena. |
| 4 | | El sistema devuelve el token y permite el acceso. |

### Excepciones
| # | Acción (actor) | Reacción (sistema) |
| :--- | :--- | :--- |
| p | El usuario introduce datos incorrectos. | El sistema devuelve error **401 Unauthorized** y pide reintentar. |

### Otros Datos
| Campo | Detalle |
| :--- | :--- |
| **Rendimiento** | La validación debe realizarse en un máximo de 2 segundos. |
| **Frecuencia** | Se espera una media de 5 veces al día por usuario. |
| **Importancia** | Vital |
| **Urgencia** | Inmediatamente |
| **Comentarios** | Es el punto de entrada obligatorio para cualquier otra acción. |