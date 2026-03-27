# 📚 Skills de Educación para Claude Code

Colección de skills personalizadas para Claude Code diseñadas específicamente para docentes. Estas skills automatizan tareas comunes del trabajo educativo: corrección, análisis de datos, creación de actividades y más.

## 🎯 Categorías de Skills

Las skills están organizadas por utilidad:

### 📋 01. Evaluación y Corrección
Skills para evaluar trabajos y proporcionar retroalimentación.

| Skill | Descripción | Comando |
|-------|-------------|---------|
| **generar-rubrica** | Crea rúbricas de evaluación detalladas con criterios y niveles | `/generar-rubrica` |
| **corregir-trabajo** | Corrige trabajos de estudiantes con feedback constructivo | `/corregir-trabajo` |

### 📊 02. Análisis de Datos
Skills para procesar información educativa.

| Skill | Descripción | Comando |
|-------|-------------|---------|
| **analizar-notas** | Analiza calificaciones y genera informes estadísticos | `/analizar-notas` |

### 🎨 03. Diseño Didáctico
Skills para crear materiales educativos.

| Skill | Descripción | Comando |
|-------|-------------|---------|
| **crear-actividad** | Diseña actividades, ejercicios y planes de clase | `/crear-actividad` |

## 🚀 Instalación

### Opción 1: Instalación en un Proyecto Específico

Copia la carpeta `.claude/skills/` al proyecto donde quieras usarlas:

```bash
# En tu proyecto
cp -r skills-educacion/.claude/skills/* .claude/skills/
```

### Opción 2: Instalación Global

Para tenerlas disponibles en todos tus proyectos:

```bash
# Windows (PowerShell)
Copy-Item -Recurse "skills-educacion/.claude/skills/*" "$env:USERPROFILE/.claude/skills/"

# Windows (Git Bash)
cp -r skills-educacion/.claude/skills/* ~/.claude/skills/

# Mac/Linux
cp -r skills-educacion/.claude/skills/* ~/.claude/skills/
```

### Opción 3: Usar desde este Repo

Clona el repositorio y usa las skills directamente:

```bash
git clone https://github.com/nesorct/mis-practicas-clase.git
cd mis-practicas-clase
```

Las skills en `.claude/skills/` se cargarán automáticamente al abrir Claude Code en este directorio.

## 📖 Uso

Una vez instaladas, puedes invocar las skills de dos formas:

### 1. Comando Directo
```
/generar-rubrica
```

### 2. Activación Automática
Las skills se activan automáticamente cuando detectan contexto relevante:
- "Necesito una rúbrica para..." → Activa `/generar-rubrica`
- "Corrige este trabajo..." → Activa `/corregir-trabajo`
- "Analiza estas notas..." → Activa `/analizar-notas`
- "Crea una actividad..." → Activa `/crear-actividad`

## 🛠️ Requisitos

- Claude Code instalado
- Acceso a las herramientas: Read, Glob, Grep, Bash (para análisis de datos)

## 📝 Ejemplos de Uso

### Generar una Rúbrica
```
/generar-rubrica
"Necesito una rúbrica para evaluar una presentación oral
sobre el tema de la Revolución Francesa en 2º de ESO,
sobre 10 puntos"
```

### Analizar Notas
```
/analizar-notas
"Analiza este archivo Excel con las calificaciones de mi clase"
```

### Corregir un Trabajo
```
/corregir-trabajo
"Corrige este ensayo sobre cambio climático de un alumno de Bachillerato"
```

### Crear Actividad
```
/crear-actividad
"Crea una actividad práctica de robótica para 1º de ESO
sobre sensores, duración 1 hora"
```

## 🔧 Estructura de una Skill

Cada skill sigue el formato oficial de Claude Code:

```markdown
---
name: nombre-skill
description: Descripción que activa la skill automáticamente
user_invocable: true
---

# Título

## Input Requerido
...

## Proceso
...

## Formato de Salida
...
```

## 🙋 Contribuir

Si tienes ideas para nuevas skills o mejoras:
1. Crea una rama con tu propuesta
2. Desarrolla la skill siguiendo el formato SKILL.md
3. Documenta su uso en este README
4. Envía un pull request

## 📄 Licencia

Este proyecto está bajo licencia MIT. Las skills son de uso libre para fines educativos.

---

**¿Preguntas?** Abre un issue en el repositorio o contacta al autor.
