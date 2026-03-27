# 📋 Evaluación y Corrección

Skills para evaluar trabajos estudiantiles y proporcionar retroalimentación efectiva.

## Skills Disponibles

### `/generar-rubrica`
Genera rúbricas de evaluación completas con criterios específicos y niveles de desempeño.

**Cuándo usarla:**
- Necesitas evaluar una actividad nueva
- Quieres estandarizar la evaluación
- Buscas criterios claros y medibles

**Inputs requeridos:**
- Actividad/tema a evaluar
- Asignatura y nivel educativo
- Puntuación máxima
- Aspectos específicos (opcional)

**Salida:**
- Tabla Markdown con criterios y niveles
- Descriptores para cada nivel (Insuficiente, Aprobado, Notable, Excelente)
- Puntuaciones asignadas
- Sugerencias de mejora

---

### `/corregir-trabajo`
Corrige trabajos de estudiantes proporcionando retroalimentación constructiva y detallada.

**Cuándo usarla:**
- Tienes trabajos para revisar
- Quieres dar feedback estructurado
- Necesitas justificar una calificación

**Inputs requeridos:**
- Trabajo del estudiante (texto, código, archivo)
- Enunciado o rúbrica original
- Tipo de trabajo y nivel educativo

**Salida:**
- Calificación global
- Lista de fortalezas
- Aspectos a mejorar con sugerencias específicas
- Recomendaciones para próximas entregas
- Recursos recomendados

---

## Ejemplo de Flujo de Trabajo

1. **Antes de la actividad:** Usa `/generar-rubrica` para crear los criterios de evaluación
2. **Durante la corrección:** Usa `/corregir-trabajo` para revisar cada entrega
3. **Después:** Comparte las rúbricas con los estudiantes para transparencia

## Consejos de Uso

- Genera la rúbrica **antes** de asignar el trabajo para tener criterios claros
- Comparte la rúbrica con los estudiantes al inicio (evaluación transparente)
- Guarda las rúbricas generadas para usarlas en futuras ocasiones
- Usa el mismo formato de corrección para mantener consistencia
