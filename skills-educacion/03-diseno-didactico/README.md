# 🎨 Diseño Didáctico

Skills para crear actividades, materiales educativos y planificar clases efectivas.

## Skills Disponibles

### `/crear-actividad`
Diseña actividades educativas completas con fases de apertura, desarrollo y cierre, incluyendo adaptaciones para diferenciación.

**Cuándo usarla:**
- Preparando una clase nueva
- Necesitas una dinámica específica
- Buscas ideas para practicar un concepto
- Quieres diferenciar para diversidad de alumnos

**Inputs requeridos:**
- Tema/contenido a enseñar
- Asignatura y nivel educativo
- Duración disponible
- Recursos disponibles (opcional)
- Tipo de actividad preferida (opcional)

**Salida:**
- Ficha técnica completa
- Objetivos de aprendizaje (saber, hacer, ser)
- Desarrollo en 3 fases (Apertura, Desarrollo, Cierre)
- Adaptaciones para estudiantes con dificultades
- Extensiones para estudiantes avanzados
- Criterios de evaluación

---

## Tipos de Actividades que Puede Generar

### Por Metodología
- **Aprendizaje Basado en Proyectos (ABP)**
- **Rotación de Estaciones**
- **Aprendizaje Cooperativo**
- **Gamificación**
- **Flipped Classroom**

### Por Recurso
- **Digitales:** Uso de apps, programación, RV/RA
- **Prácticas:** Experimentos, manipulativos
- **Colaborativas:** Debates, juegos de rol, mosaico
- **Evaluativas:** Entradas/salidas, cuadernos interactivos

---

## Ejemplos de Uso

### Actividad Práctica
```
/crear-actividad
"Crea una actividad práctica sobre direccionamiento IP para
1º de Bachillerato. Tengo ordenadores y 1 hora."
```

### Actividad Gamificada
```
/crear-actividad
"Necesito una escape room digital para repasar conceptos de
robótica antes del examen. Nivel: 1º de ESO."
```

### Actividad Diferenciada
```
/crear-actividad
"Diseña una actividad sobre el ciclo del agua para 5º de
Primaria que incluya adaptaciones para un alumno con TDAH
y extensiones para alumnos avanzados."
```

### Proyecto Interdisciplinar
```
/crear-actividad
"Crea un proyecto de 4 sesiones que combine Tecnología e
Inglés: crear un video explicativo sobre una invención
tecnológica. Nivel: 3º de ESO."
```

---

## Elementos de una Buena Actividad

Una actividad generada por esta skill incluye:

1. **Apertura impactante** (10-15% tiempo)
   - Ganchos motivadores
   - Conexión con conocimientos previos
   - Presentación de objetivos

2. **Desarrollo estructurado** (60-70% tiempo)
   - Instrucciones claras paso a paso
   - Práctica guiada e independiente
   - Puntos de verificación

3. **Cierre efectivo** (15-20% tiempo)
   - Puesta en común
   - Reflexión metacognitiva
   - Conexión con vida real

4. **Diferenciación incluida**
   - Adaptaciones para dificultades
   - Extensiones para avanzados

---

## Consejos de Uso

- Sé **específico** en los inputs para obtener mejores resultados
- **Adapta** la actividad generada a tu contexto real
- **Prueba** la actividad antes de implementarla
- **Documenta** qué actividades funcionan mejor para reutilizarlas
- **Combina** esta skill con `/generar-rubrica` para tener también criterios de evaluación
