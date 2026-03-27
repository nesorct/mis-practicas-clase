# 📚 Proyecto de Prácticas Educativas

Repositorio personal de prácticas, proyectos y herramientas educativas.

## 📁 Estructura del Repositorio

```
/
├── README.md                          ← Este archivo
├── skills-educacion/                  ← 🎓 Skills para Claude Code
│   ├── 01-evaluacion-correccion/      │   ├── generar-rubrica
│   │   └── corregir-trabajo           │
│   ├── 02-analisis-datos/             │   │   └── analizar-notas
│   └── 03-diseno-didactico/           │   │       └── crear-actividad
├── herramientas-docentes/             ← 🛠️ Scripts y utilidades
│   └── classroom_students.py          │       Script para Google Classroom
├── practicas-alumnos/                 ← 👨‍🎓 Trabajos de estudiantes
│   ├── CREACION EMPRESA/
│   ├── DIRECCIONAMIENTO IP/
│   ├── HOJAS DE CÁLCULO - PRÁCTICA 1/
│   ├── PRACTICA 1 DE ROBÓTICA/
│   ├── PRACTICA 2 DE ROBÓTICA/
│   ├── PRACTICA 3 ROBÓTICA/
│   ├── PRACTICA 4 DE ROBÓTICA/
│   ├── PROYECTO METEORITO 2ª EV/
│   ├── REDES INFORMÁTICAS/
│   └── TAREA EXTRA DE DIRECCIONAMIENTO IP/
└── .claude/skills/                    ← Skills activas (uso local)
```

## 🎓 Skills de Educación

Este repositorio incluye **skills personalizadas para Claude Code** que automatizan tareas docentes.

### ¿Qué son las Skills?

Las skills son instrucciones predefinidas que permiten a Claude Code realizar tareas específicas de forma automatizada.

### Skills Disponibles

| Categoría | Skill | Descripción | Comando |
|-----------|-------|-------------|---------|
| **Evaluación** | generar-rubrica | Crea rúbricas de evaluación | `/generar-rubrica` |
| **Evaluación** | corregir-trabajo | Corrige con feedback | `/corregir-trabajo` |
| **Datos** | analizar-notas | Analiza calificaciones | `/analizar-notas` |
| **Diseño** | crear-actividad | Crea actividades | `/crear-actividad` |

📖 [Ver documentación completa de skills](skills-educacion/README.md)

### Instalación Rápida

#### Opción 1: Uso Local (Proyecto Actual)
Las skills en `.claude/skills/` ya están activas en este proyecto. Solo abre Claude Code aquí y usa:
```
/generar-rubrica
/corregir-trabajo
/analizar-notas
/crear-actividad
```

#### Opción 2: Instalar en Otro Proyecto
Copia las skills a tu nuevo proyecto:
```bash
cp -r skills-educacion/.claude/skills/* tu-proyecto/.claude/skills/
```

#### Opción 3: Instalación Global
Para usarlas en cualquier proyecto:
```bash
# Windows (Git Bash)
cp -r skills-educacion/.claude/skills/* ~/.claude/skills/

# Mac/Linux
cp -r skills-educacion/.claude/skills/* ~/.claude/skills/
```

## 👨‍🏫 Sobre el Autor

**Profesor:** Jaime Aniorte Garcia
**Email:** jaimeaniorte.garcia@gmail.com
**Institución:** (Añadir si es público)

Materias que imparte:
- Robótica / Tecnología
- Redes Informáticas
- Digitalización / Hojas de Cálculo
- Creación de Empresas

## 🛠️ Herramientas Incluidas

### `classroom_students.py`
Script de Python para obtener la lista de alumnos de Google Classroom y guardarla en un archivo de texto.

**Uso:**
```bash
python classroom_students.py
```

**Requisitos:**
- Credenciales de Google Cloud (archivo `client_secret_*.json`)
- Permisos de acceso a Google Classroom API
- Python 3.x con dependencias: `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, `google-api-python-client`

⚠️ **Nota:** El archivo de credenciales NO está incluido en el repositorio por seguridad (ver `.gitignore`).

## 📂 Prácticas de Alumnos

Carpetas con trabajos entregados por estudiantes organizados por tema:

- **CREACION EMPRESA** - Documentos de plan de empresa
- **DIRECCIONAMIENTO IP** - Ejercicios de redes
- **HOJAS DE CÁLCULO** - Prácticas de Excel
- **PRACTICA 1-4 DE ROBÓTICA** - Actividades de programación
- **PROYECTO METEORITO** - Proyecto de evaluación
- **REDES INFORMÁTICAS** - Configuraciones y esquemas

## 🔒 Seguridad

El archivo `.gitignore` está configurado para proteger:
- Credenciales de Google (`client_secret_*.json`, `token.json`)
- Archivos generados por Python (`__pycache__`, `*.pyc`)
- Archivos de sistema (`.DS_Store`, `Thumbs.db`)

**Nunca subas credenciales a GitHub.**

## 📜 Licencia

Este repositorio es de uso personal y educativo. Las skills pueden usarse libremente en proyectos educativos.

## 🚀 Cómo Clonar este Repositorio

```bash
git clone https://github.com/nesorct/mis-practicas-clase.git
cd mis-practicas-clase
```

---

**¿Preguntas o sugerencias?** Abre un issue en GitHub o contacta al autor.
