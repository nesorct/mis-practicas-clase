# 🦙 n8n + Ollama LOCAL (Windows)

Guía para conectar n8n en Docker con **Ollama que ya tienes instalado** en tu PC Windows.

## ✅ Requisitos

- ✅ Ollama instalado en tu PC Windows
- ✅ Modelos descargados: `mistral`, `llama3`, `qwen3.5:0.8b`, `gemma3:1b`
- ✅ Docker Desktop instalado
- ✅ Windows 10/11

## 🚀 Instrucciones Paso a Paso

### Paso 1: Configurar Ollama para Aceptar Conexiones

Por defecto, Ollama en Windows solo acepta conexiones locales. Necesitamos que acepte conexiones desde Docker.

**Abre PowerShell y ejecuta:**

```powershell
# Configurar variable de entorno (se guarda para siempre)
[Environment]::SetEnvironmentVariable("OLLAMA_HOST", "0.0.0.0", "User")

# Reiniciar Ollama
ollama stop
# Espera unos segundos...
ollama serve
```

**Verifica que está corriendo:**
```powershell
curl http://localhost:11434/api/tags
```

Debería mostrar tus modelos instalados.

**Deja esta ventana abierta** (Ollama debe seguir corriendo).

---

### Paso 2: Configurar Variables de Entorno

Copia el archivo `.env.example` a `.env`:

```powershell
copy .env.example .env
```

Edita el archivo `.env` y asegúrate de tener:

```env
# Seguridad (CAMBIA ESTOS VALORES)
N8N_ENCRYPTION_KEY=openssl rand -hex 32  # Genera esto primero
N8N_BASIC_AUTH_PASSWORD=tu_contraseña_segura

# Configuración básica
N8N_HOST=localhost
N8N_PROTOCOL=http
WEBHOOK_URL=http://localhost:5678/
GENERIC_TIMEZONE=Europe/Madrid

# Base de datos PostgreSQL
POSTGRES_USER=n8n
POSTGRES_PASSWORD=postgres_password_segura
POSTGRES_DB=n8n

# OLLAMA (usa tu Ollama local en Windows)
OLLAMA_HOST=http://host.docker.internal:11434

# No necesitas API keys de pago con Ollama local
```

**Para generar N8N_ENCRYPTION_KEY:**
```powershell
openssl rand -hex 32
```

Copia el resultado y pégalo en el archivo `.env`.

---

### Paso 3: Iniciar n8n con Docker

**Abre otra terminal de PowerShell** (no cierres la que tiene Ollama corriendo) y ejecuta:

```powershell
# Navega a la carpeta del proyecto
cd C:\Users\JAIME\Desktop\vs code

# Iniciar servicios
docker-compose -f docker-compose-n8n-local-ollama.yml up -d
```

Esto iniciará:
- n8n (puerto 5678)
- PostgreSQL (base de datos)
- Redis (colas)

**Verifica que todo está corriendo:**
```powershell
docker ps
```

Deberías ver 3 contenedores: postgres, redis, n8n.

---

### Paso 4: Verificar Conexión con Ollama

Prueba que n8n puede conectar con Ollama:

```powershell
# Entra al contenedor de n8n
docker exec -it n8n-n8n-1 /bin/sh

# Prueba la conexión con Ollama
curl http://host.docker.internal:11434/api/tags

# Debería mostrar tus modelos:
# {"models":[{"name":"mistral:latest"...}

# Salir del contenedor
exit
```

Si ves tus modelos, ¡todo está configurado correctamente!

---

### Paso 5: Acceder a n8n

1. Abre tu navegador: http://localhost:5678
2. Inicia sesión con:
   - Usuario: `admin` (o el que pusiste en N8N_BASIC_AUTH_USER)
   - Contraseña: la que pusiste en N8N_BASIC_AUTH_PASSWORD

---

## 🛠️ Configurar tu Primer Workflow con Ollama

### Paso 6: Crear Workflow de Prueba

1. En n8n, haz clic en **"Add Workflow"**
2. Añade un nodo **"Webhook"**:
   - Method: POST
   - Path: `test-ollama`
   - Response Mode: Last Node

3. Añade un nodo **"HTTP Request"** después del Webhook:

   **Configuración:**
   ```
   Method: POST
   URL: http://host.docker.internal:11434/api/generate

   Headers:
     Content-Type: application/json

   Body (JSON):
   {
     "model": "mistral",
     "prompt": "Resume este texto en español: {{ $json.body.texto }}",
     "stream": false
   }
   ```

4. Añade un nodo **"Respond to Webhook"** al final:
   - Body:
   ```json
   {
     "respuesta": "{{ $json.response }}"
   }
   ```

5. Guarda el workflow (Ctrl+S)

6. Activa el workflow (Toggle "Inactive" → "Active")

---

### Paso 7: Probar el Workflow

**Prueba con curl:**
```powershell
curl -X POST http://localhost:5678/webhook/test-ollama `
  -H "Content-Type: application/json" `
  -d '{"texto": "La inteligencia artificial está transformando la educación moderna permitiendo personalización del aprendizaje y automatización de tareas administrativas para los profesores."}'
```

**O con Postman/Insomnia:**
- URL: POST http://localhost:5678/webhook/test-ollama
- Body (JSON):
```json
{
  "texto": "Tu texto aquí para que Ollama lo procese"
}
```

Deberías recibir una respuesta de Ollama procesando tu texto.

---

## 🎓 Workflows Educativos de Ejemplo

### Ejemplo 1: Corrector de Trabajos

```
Webhook (trabajo estudiante) → HTTP Request (Ollama con mistral) → Email (resultado)
```

**Prompt en Ollama:**
```json
{
  "model": "mistral",
  "prompt": "Actúa como profesor de secundaria. Corrige este trabajo:\n\n{{ $json.body.trabajo }}\n\nProporciona:\n1. Calificación sobre 10\n2. 2 fortalezas\n3. 2 áreas de mejora\n4. Comentario constructivo final",
  "stream": false
}
```

---

### Ejemplo 2: Generador de Actividades

```
Formulario (tema, nivel, duración) → HTTP Request (Ollama) → Google Docs
```

**Prompt:**
```json
{
  "model": "llama3",
  "prompt": "Crea una actividad educativa:\n\nTema: {{ $json.body.tema }}\nNivel: {{ $json.body.nivel }}\nDuración: {{ $json.body.duracion }}\n\nIncluye:\n1. Objetivos de aprendizaje\n2. Materiales necesarios\n3. Desarrollo paso a paso\n4. Criterios de evaluación",
  "stream": false
}
```

---

### Ejemplo 3: Análisis de Datos Simple

```
Webhook (datos CSV en texto) → HTTP Request (Ollama) → Slack/Email
```

**Prompt:**
```json
{
  "model": "mistral",
  "prompt": "Analiza estos datos de calificaciones y proporciona:\n\n{{ $json.body.datos }}\n\n1. Resumen estadístico (media, máximo, mínimo)\n2. Tasa de aprobación\n3. 3 observaciones relevantes\n4. 2 recomendaciones para el docente",
  "stream": false
}
```

---

## 🔧 Uso de Modelos Diferentes

Tienes 4 modelos disponibles. Úsalos según la tarea:

| Modelo | Tarea | Prompt de ejemplo |
|--------|-------|-------------------|
| **mistral** | Corrección de trabajos complejos | `"model": "mistral"` |
| **llama3** | Generación de contenido educativo | `"model": "llama3"` |
| **qwen3.5:0.8b** | Respuestas rápidas, tareas simples | `"model": "qwen3.5:0.8b"` |
| **gemma3:1b** | Clasificación, resúmenes ultra-rápidos | `"model": "gemma3:1b"` |

---

## ❓ Troubleshooting

### Error: "Connection refused" o "Cannot connect"

**Solución:**
1. Verifica que Ollama sigue corriendo:
   ```powershell
   curl http://localhost:11434/api/tags
   ```

2. Verifica que Ollama está en modo 0.0.0.0:
   ```powershell
   [Environment]::GetEnvironmentVariable("OLLAMA_HOST", "User")
   # Debe mostrar: 0.0.0.0
   ```

3. Reinicia Ollama si es necesario.

### Error: "model not found"

**Solución:** Verifica el nombre exacto del modelo:
```powershell
ollama list
# Usa exactamente el nombre que aparece, ej: "mistral:latest" o "llama3:latest"
```

### Error: Docker no puede conectar a host.docker.internal

**Solución:** Asegúrate de estar usando `docker-compose-n8n-local-ollama.yml` (no el de Ollama Pro).

### n8n tarda mucho en responder

**Solución:** Aumenta el timeout en el nodo HTTP Request:
- Ve a Settings → Timeout
- Pon 120000 (2 minutos) o más

---

## 🛑 Detener Todo

Cuando termines, detén los servicios:

```powershell
# Detener n8n
docker-compose -f docker-compose-n8n-local-ollama.yml down

# Ollama sigue corriendo (puedes dejarlo)
# Para detener Ollama también:
ollama stop
```

---

## 🔄 Reiniciar Todo

La próxima vez que quieras usarlo:

1. **Inicia Ollama** (en una terminal):
   ```powershell
   $env:OLLAMA_HOST="0.0.0.0"
   ollama serve
   ```

2. **Inicia n8n** (en otra terminal):
   ```powershell
   docker-compose -f docker-compose-n8n-local-ollama.yml up -d
   ```

3. Abre http://localhost:5678

---

## 📚 Recursos

- [Documentación Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Documentación n8n](https://docs.n8n.io/)
- [Workflows de ejemplo en n8n](https://n8n.io/workflows)

---

**¿Listo para empezar?** Ve al Paso 1 y dime si tienes algún problema. 🚀
