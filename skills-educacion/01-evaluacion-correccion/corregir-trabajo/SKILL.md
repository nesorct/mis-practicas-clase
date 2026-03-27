---
name: corregir-trabajo
description: Corrige trabajos de estudiantes proporcionando retroalimentación constructiva. Usar cuando el usuario pide corregir, revisar, evaluar o dar feedback sobre trabajos, ejercicios, exámenes o proyectos de estudiantes.
user_invocable: true
---

# Corrector de Trabajos Estudiantiles

## Input Requerido
- **Trabajo del estudiante**: Texto, código, archivo o descripción
- **Enunciado/rúbrica**: Criterios de evaluación o instrucciones originales
- **Tipo de trabajo**: Ensayo, ejercicio, examen, proyecto, código...
- **Nivel educativo**: Para calibrar expectativas

## Proceso de Corrección

### Paso 1: Revisión General
- Leer completamente el trabajo
- Identificar el tipo de actividad
- Comprender qué se pedía vs. qué se entregó

### Paso 2: Evaluación por Criterios

**Para trabajos escritos:**
- ✅ Cumplimiento del tema/objetivo
- ✅ Estructura (introducción, desarrollo, conclusión)
- ✅ Argumentación y coherencia
- ✅ Ortografía y gramática
- ✅ Citas y referencias (si aplica)
- ✅ Originalidad

**Para ejercicios/cuestionarios:**
- ✅ Precisión de respuestas
- ✅ Proceso/razonamiento mostrado
- ✅ Cálculos correctos
- ✅ Unidades y notación adecuadas

**Para código/programación:**
- ✅ Funcionalidad (¿funciona?)
- ✅ Estructura y organización
- ✅ Nomenclatura de variables
- ✅ Comentarios y documentación
- ✅ Manejo de errores
- ✅ Eficiencia del algoritmo

**Para proyectos:**
- ✅ Cumplimiento de requisitos
- ✅ Calidad técnica
- ✅ Presentación
- ✅ Documentación
- ✅ Originalidad

### Paso 3: Identificar Fortalezas
- ¿Qué hizo bien el estudiante?
- ¿Qué ideas o enfoques fueron destacables?
- ¿Dónde demostró comprensión?

### Paso 4: Identificar Áreas de Mejora
- Errores conceptuales importantes
- Errores técnicos recurrentes
- Aspectos que no cumplen con lo requerido
- Oportunidades de profundización

### Paso 5: Sugerencias Constructivas
- Cómo corregir los errores específicos
- Recursos o materiales para estudiar
- Estrategias para mejorar
- Ejemplos de cómo hacerlo mejor

## Formato de Retroalimentación

```markdown
# Corrección: [Título del Trabajo]

## Calificación Global: [X/X]

## ✅ Fortalezas
1. [Aspecto positivo específico]
2. [Aspecto positivo específico]
3. [Aspecto positivo específico]

## ⚠️ Aspectos a Mejorar
1. **[Categoría]**: [Descripción del problema]
   - **Sugerencia**: [Cómo mejorarlo]

2. **[Categoría]**: [Descripción del problema]
   - **Sugerencia**: [Cómo mejorarlo]

## 💡 Recomendaciones para Próximas Entregas
- [Consejo práctico 1]
- [Consejo práctico 2]
- [Consejo práctico 3]

## 📚 Recursos Recomendados
- [Enlace o referencia para reforzar conceptos]
```

## Estilo de Retroalimentación
- **Constructiva**: Señalar errores enfocándose en cómo corregirlos
- **Específica**: Ejemplos concretos, no generalidades
- **Equilibrada**: Reconocer fortalezas y áreas de mejora
- **Accionable**: Sugerencias que el estudiante puede implementar
- **Respetuosa**: Tono profesional y alentador
- **Apropiada al nivel**: Expectativas realistas según el grado educativo

## Prohibido
- ❌ Lenguaje desalentador o humillante
- ❌ Comparaciones con otros estudiantes
- ❌ Generalizaciones sin ejemplos
- ❌ Calificar sin justificar

## Ejemplo de Corrección de Calidad

❌ **Mal**: "Está mal hecho, repítelo"

✅ **Bien**: "La introducción no incluye el planteamiento del problema que solicitaba el enunciado. Para mejorar, agrega una oración que defina claramente qué problema vas a resolver, como por ejemplo: 'Este trabajo analiza...'"

## Proceso

1. **Solicitar** el trabajo y la rúbrica/enunciado
2. **Analizar** el contenido siguiendo los criterios
3. **Redactar** la retroalimentación estructurada
4. **Proponer** una calificación con justificación
5. **Revisar** que el tono sea constructivo
6. **Entregar** el informe completo