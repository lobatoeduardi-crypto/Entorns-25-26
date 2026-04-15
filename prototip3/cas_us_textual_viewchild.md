# Caso de Uso Textual: VIEWCHILD

**Actor principal:** Tutor, Cuidador y Administrador

**Descripción:** Acceso a recurso protegido para ver los datos de los niños (Childs).

**Precondición:** El usuario debe estar Autenticado con un token válido.

**Postcondición:** El sistema muestra la información de los niños asociados al usuario.

**Flujo principal:**
1. El usuario solicita acceder a "Childs".
2. El sistema envía la petición junto con el Token de seguridad.
3. El servidor valida que el Token sea correcto y no haya expirado.
4. El servidor recupera los datos de la BBDD.
5. El sistema muestra la lista de niños al usuario.

**Flujos alternativos:**
* **Token inválido:** Si el token no es correcto, el servidor devuelve un error y deniega el acceso.