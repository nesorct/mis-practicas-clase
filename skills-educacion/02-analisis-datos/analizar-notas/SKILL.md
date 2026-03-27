---
name: analizar-notas
description: Analiza datos de calificaciones y genera informes estadísticos. Usar cuando el usuario pide analizar notas, examinar resultados, estadísticas de clase, identificar tendencias o generar informes de evaluación.
user_invocable: true
---

# Analizador de Calificaciones y Datos Educativos

## Input Requerido
- **Archivo de datos**: CSV, Excel, o lista de notas
- **Escala de evaluación**: ¿Sobre qué se evalúa? (ej. 0-10, A-F, porcentaje)
- **Umbral de aprobado**: ¿Cuál es la nota mínima para aprobar?
- **Contexto**: ¿Es un examen, trimestre, proyecto...?

## Análisis a Realizar

### 1. Estadísticas Descriptivas
- **Media** (promedio)
- **Mediana** (nota central)
- **Moda** (nota más frecuente)
- **Desviación estándar** (dispersión de notas)
- **Nota máxima y mínima**
- **Rango** (diferencia entre max y min)

### 2. Distribución de Calificaciones
Clasifica estudiantes en:
- **Sobresaliente**: ≥9 (90%)
- **Notable**: 7-8.9 (70-89%)
- **Aprobado**: 5-6.9 (50-69%)
- **Suspenso**: <5 (<50%)

Muestra:
- Cantidad y porcentaje en cada rango
- Representación visual (ASCII chart o descripción)

### 3. Análisis de Aprobación
- **Tasa de aprobación**: % que superan el umbral
- **Tasa de suspensión**: % por debajo del umbral
- **Media de aprobados** vs **media de suspensos**
- **Estudiantes en riesgo**: Nota <4 (requieren atención urgente)

### 4. Identificación de Patrones
- ¿Hay valores atípicos (outliers)?
- ¿La distribución es normal o sesgada?
- ¿Hay grupos de estudiantes con dificultades similares?
- Comparación con evaluaciones anteriores (si hay datos)

## Formato de Salida

```markdown
# Informe de Análisis de Calificaciones

## Resumen Ejecutivo
- Total de estudiantes: [N]
- Media de la clase: [X.X]
- Tasa de aprobación: [X]% ([N] de [Total])

## Estadísticas Descriptivas
| Métrica | Valor |
|---------|-------|
| Media | X.XX |
| Mediana | X.XX |
| Moda | X.XX |
| Desv. Estándar | X.XX |
| Mínimo | X.XX |
| Máximo | X.XX |

## Distribución por Rangos
| Rango | Cantidad | Porcentaje |
|-------|----------|------------|
| Sobresaliente | X | X% |
| Notable | X | X% |
| Aprobado | X | X% |
| Suspenso | X | X% |

## Estudiantes que Requieren Atención
[Lista de estudiantes con nota < 4 y sugerencias]

## Recomendaciones Docentes
1. [Basada en el análisis]
2. [Intervención sugerida]
```

## Herramientas Disponibles
- Read: Para leer archivos CSV/Excel
- Grep: Para filtrar datos específicos
- Bash: Para procesamiento de datos si es necesario

## Proceso

1. **Leer** el archivo de datos proporcionado
2. **Extraer** las notas y organizarlas
3. **Calcular** todas las estadísticas
4. **Clasificar** estudiantes según rangos
5. **Identificar** patrones y anomalías
6. **Generar** recomendaciones pedagógicas
7. **Presentar** el informe completo formateado

## Consideraciones Éticas
- Mantener la confidencialidad de los datos
- No compartir nombres si el usuario no lo solicita explícitamente
- Usar IDs o códigos en lugar de nombres cuando sea posible
- Enfocar el análisis en patrones grupales, no en señalar individualmente