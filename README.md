# El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas

**Integrantes:** James Rizzo
**Fecha:** 28 de junio de 2026

### Objetivo del sistema
Automatizar y validar el registro de calificaciones de estudiantes, minimizando errores de cálculo manual y evitando la pérdida de información mediante la implementación de persistencia de datos en memoria local.

### Descripción de funcionalidades
1. **Registro validado:** Permite ingresar estudiantes asegurando mediante bucles y manejo de excepciones que las notas sean estrictamente numéricas y estén en el rango de 0 a 10.
2. **Visualización de datos:** Muestra el registro completo de estudiantes organizados en un formato de tabla estructurada en consola.
3. **Búsqueda exacta:** Permite localizar el estado académico de un estudiante específico mediante su nombre.
4. **Cálculo automatizado:** Genera el promedio general de todo el curso al instante.
5. **Persistencia de datos:** Utiliza la librería nativa `json` para guardar automáticamente la información, evitando que los registros se borren al cerrar el programa.
