| Caso de prueba | Entrada | Salida esperada | Salida obtenida | Resultado (OK/BUG) |
|----------------|---------|----------------|----------------|-------------------|
| Insertar usuario nuevo | (1, "Alice") | Usuario agregado | ? | ? |
| Insertar usuario duplicado | (2, "Bob"), (2, "Charlie") | Error o rechazo | ? | ? |
| Buscar usuario | ID=2 | "Bob" | ? | ? |
| Eliminar usuario duplicado | ID=2 | Elimina todos | ? | ? |
| Listar nombres | Usuarios actuales | ["Alice", ...] | ? | ? |
| Promedio en lista vacía | [] | Error controlado | ? | ? |
