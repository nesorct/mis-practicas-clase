# 📊 Análisis de Datos

Skills para procesar información educativa y obtener insights sobre el rendimiento estudiantil.

## Skills Disponibles

### `/analizar-notas`
Analiza datos de calificaciones y genera informes estadísticos completos con visualizaciones y recomendaciones.

**Cuándo usarla:**
- Fin de trimestre/evaluación
- Quieres identificar patrones de rendimiento
- Necesitas datos para reuniones con padres o tutorías
- Quieres comparar resultados entre evaluaciones

**Inputs requeridos:**
- Archivo de datos (CSV, Excel, lista)
- Escala de evaluación (0-10, A-F, porcentaje)
- Umbral de aprobado

**Salida:**
- Estadísticas descriptivas (media, mediana, desviación estándar)
- Distribución por rangos (Sobresaliente, Notable, Aprobado, Suspenso)
- Tasa de aprobación y suspensión
- Estudiantes en riesgo (atención prioritaria)
- Recomendaciones docentes basadas en los datos

---

## Ejemplos de Uso

### Análisis de Examen
```
/analizar-notas
"Analiza el archivo examen-parcial.xlsx con las notas de mi
curso. La escala es 0-10 y el aprobado es 5."
```

### Comparativa Trimestral
```
/analizar-notas
"Compara las notas de este trimestre con las del trimestre
anterior. Tengo los datos en notas-trimestre-1.csv y
notas-trimestre-2.csv"
```

### Identificación de Estudiantes en Riesgo
```
/analizar-notas
"Analiza estas calificaciones y dime qué estudiantes necesitan
atención prioritaria (notas < 4)"
```

---

## Consejos de Uso

- **Privacidad:** No compartas nombres completos en contextos públicos. Usa códigos o IDs.
- **Temporalidad:** Analiza datos regularmente (mensual/trimestral) para detectar tendencias temprano
- **Comparativas:** Guarda los análisis anteriores para hacer comparativas evolutivas
- **Acción:** Usa el apartado "Recomendaciones docentes" para planificar intervenciones

## Privacidad y Ética

⚠️ **Importante:** Los datos de estudiantes son sensibles. Recuerda:
- Mantener la confidencialidad
- No compartar nombres en foros públicos
- Cumplir con la normativa de protección de datos (RGPD)
- Usar el análisis para mejorar la enseñanza, no para etiquetar estudiantes
