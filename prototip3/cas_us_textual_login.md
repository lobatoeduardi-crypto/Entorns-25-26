### La descripción detallada en texto del proceso de entrada.

```markdown
# Caso de Uso Textual: LOGIN

**Actor principal:** Tutor, Cuidador y Administrador

**Descripción:** Permite al usuario autenticarse mediante credenciales.

**Precondición:** El usuario debe estar Registrado.

**Postcondición:** El usuario queda autenticado con un token válido.

**Flujo principal:**
1. El usuario envía `username` y `password`.
2. El servidor valida las credenciales.
3. El servidor genera un token.
4. El token se almacena en la BBDD.
5. El servidor devuelve al cliente el token y datos del usuario.

**Flujos alternativos:**
* **Error de autenticación:** Si las credenciales son incorrectas, se devuelve un error **401 Unauthorized**.