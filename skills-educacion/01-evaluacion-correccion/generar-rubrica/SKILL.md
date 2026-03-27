---
name: generar-rubrica
description: Genera rúbricas de evaluación detalladas para cualquier actividad educativa. Usar cuando el usuario pide crear una rúbrica, criterios de evaluación, escala de calificación o matriz de evaluación.
user_invocable: true
---

# Generador de Rúbricas de Evaluación

## Input Requerido
- **Actividad/Trabajo**: ¿Qué van a hacer los estudiantes?
- **Asignatura/Materia**: ¿En qué contexto se evalúa?
- **Nivel educativo**: Primaria, ESO, Bachillerato, Universidad...
- **Puntuación máxima**: ¿Sobre cuánto se evalúa? (ej. 10 puntos)
- **Aspectos a evaluar**: Competencias específicas (opcional)

## Estructura de la Rúbrica

Crea una rúbrica con:

### 1. Encabezado
- Nombre de la actividad
- Asignatura y nivel
- Puntuación total
- Fecha/periodo

### 2. Criterios de Evaluación (4-6 criterios)
Cada criterio debe tener:
- **Descriptor** (qué se evalúa)
- **Peso/puntuación** asignada
- **4 niveles de desempeño**:
  - Excelente (90-100%): Descripción detallada
  - Notable (75-89%): Descripción detallada
  - Aprobado (60-74%): Descripción detallada
  - Insuficiente (0-59%): Descripción detallada

### 3. Criterios Sugeridos por Tipo de Actividad

**Para trabajos escritos:**
- Contenido y desarrollo de ideas
- Estructura y organización
- Ortografía y gramática
- Originalidad y creatividad
- Cumplimiento de requisitos

**Para presentaciones orales:**
- Contenido y dominio del tema
- Expresión oral y claridad
- Recursos visuales
- Organización temporal
- Participación/Interacción

**Para proyectos:**
- Planificación y organización
- Ejecución técnica
- Creatividad e innovación
- Documentación
- Presentación de resultados

**Para prácticas tecnológicas:**
- Correcta aplicación de procedimientos
- Precisión técnica
- Resolución de problemas
- Organización y orden
- Comprensión conceptual

### 4. Formato de Salida

Presenta la rúbrica en formato tabla Markdown:

```markdown
| Criterio | Insuficiente (0-X) | Aprobado (X-Y) | Notable (Y-Z) | Excelente (Z-Total) | Puntos |
|----------|-------------------|----------------|---------------|---------------------|--------|
| Criterio 1 | [descripción] | [descripción] | [descripción] | [descripción] | X pts |
```

## Ejemplo de Nivel Excelente
Cada descriptor de nivel excelente debe ser:
- Específico y observable
- Medible
- Alcanzable pero desafiante
- Descrito con verbos de acción

## Proceso

1. **Preguntar** al usuario los datos requeridos si no los proporcionó
2. **Sugerir** criterios apropiados para el tipo de actividad
3. **Desarrollar** descriptores para cada nivel
4. **Revisar** que la suma de puntos sea correcta
5. **Entregar** la rúbrica formateada y lista para usar

## Notas Importantes
- Adapta el lenguaje al nivel educativo (más simple para primaria, más técnico para universidad)
- Incluye una fila de puntuación total
- Ofrece la opción de exportar a Excel o PDF si el usuario lo solicita