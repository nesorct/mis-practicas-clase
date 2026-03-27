# 🦙 n8n + Ollama (Modelos Locales) - Setup 100% Gratuito

Configuración de n8n con **Ollama** para usar modelos de IA locales (Llama, Mistral, etc.) sin pagar por APIs externas.

## 🎯 ¿Por qué Ollama?

- ✅ **100% Gratis** - Sin costos de API
- ✅ **100% Privado** - Tus datos nunca salen del servidor
- ✅ **Sin límites** - Usa los modelos todo lo que quieras
- ✅ **Offline** - Funciona sin conexión a internet
- ✅ **Sin rate limits** - No hay restricciones de uso

## 📋 Requisitos de Hardware

| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| **RAM** | 8 GB | 16 GB+ |
| **CPU** | 4 cores | 8 cores modernos |
| **GPU** | No requerida | NVIDIA 8GB+ VRAM (opcional) |
| **Disco** | 20 GB libre | 50 GB+ SSD |

**Nota:** Sin GPU, los modelos corren en CPU (más lento pero funciona).

## 🚀 Instalación

### Paso 1: Descargar Archivos

Descarga estos archivos a tu servidor:
- `docker-compose-n8n-ollama.yml`
- `.env.example` (puedes reusar el mismo)
- `redis.conf`

### Paso 2: Configurar Variables de Entorno

```bash
# Copia el archivo de ejemplo
cp .env.example .env

# Edita con tus valores
nano .env
```

**Variables importantes:**
```env
# Seguridad (obligatorio)
N8N_ENCRYPTION_KEY=openssl rand -hex 32
N8N_BASIC_AUTH_PASSWORD=tu_contraseña_segura

# NO necesitas ANTHROPIC_API_KEY ni OPENAI_API_KEY
# (deja estas líneas comentadas o elimínalas)

# Configuración básica
N8N_HOST=localhost
GENERIC_TIMEZONE=Europe/Madrid
```

### Paso 3: Iniciar Servicios

```bash
docker-compose -f docker-compose-n8n-ollama.yml up -d
```

Esto descargará e iniciará:
- n8n (interfaz web en puerto 5678)
- Ollama (servidor de modelos en puerto 11434)
- PostgreSQL (base de datos)
- Redis (colas)

### Paso 4: Descargar un Modelo

Una vez iniciado, descarga un modelo de Ollama:

```bash
# Entrar al contenedor de Ollama
docker exec -it ollama-ollama-1 /bin/bash

# Descargar Llama 3.1 (8B - rápido, bueno para empezar)
ollama pull llama3.1

# O descargar Mistral (7B - muy capaz)
ollama pull mistral

# O descargar CodeLlama (especializado en código)
ollama pull codellama

# Ver modelos disponibles
ollama list
```

**Modelos recomendados para educación:**

| Modelo | Tamaño | Uso ideal | VRAM Requerida |
|--------|--------|-----------|----------------|
| `llama3.1:8b` | 4.7 GB | Uso general, corrección de trabajos | ~6 GB |
| `mistral:7b` | 4.1 GB | Razonamiento, análisis | ~6 GB |
| `codellama:7b` | 3.8 GB | Programación, robótica | ~5 GB |
| `llama3.1:70b` | 40 GB | Máxima calidad (requiere GPU potente) | ~80 GB |

**Para CPU (sin GPU):**
- Usa modelos más pequeños: `llama3.1:8b`, `mistral:7b`
- Serán más lentos pero funcionan

### Paso 5: Configurar n8n

1. Abre n8n: http://localhost:5678
2. Inicia sesión con las credenciales del `.env`
3. Crea un nuevo workflow
4. Añade un nodo **HTTP Request** para conectar con Ollama:

**Configuración del nodo HTTP Request:**

```
Method: POST
URL: http://ollama:11434/api/generate

Headers:
  Content-Type: application/json

Body (JSON):
{
  "model": "llama3.1",
  "prompt": "{{ $json.prompt }}",
  "stream": false
}
```

**O para chat con historial:**

```
Method: POST
URL: http://ollama:11434/api/chat

Body (JSON):
{
  "model": "llama3.1",
  "messages": [
    {"role": "system", "content": "Eres un profesor experto."},
    {"role": "user", "content": "{{ $json.pregunta }}"}
  ],
  "stream": false
}
```

## 🔧 Usar Ollama en n8n

### Opción 1: HTTP Request Node (Manual)

Como se muestra arriba, usando el endpoint HTTP de Ollama.

### Opción 2: Ollama Credential (Más fácil)

1. En n8n, ve a **Settings → Credentials**
2. Clic en **Add Credential**
3. Busca "Ollama" (puede requerir instalar el nodo)
4. Configura:
   - **Base URL**: `http://ollama:11434`
   - **Model**: `llama3.1` (o el que descargaste)

### Opción 3: Custom Node (Avanzado)

Instala el nodo community de Ollama:
```bash
docker exec n8n-n8n-1 npm install n8n-nodes-ollama
```

## 📊 Comparativa de Modelos

| Modelo | Tareas Educativas | Velocidad (CPU) | Calidad |
|--------|-------------------|-----------------|---------|
| **Llama 3.1 8B** | Excelente | Media | ⭐⭐⭐⭐ |
| **Mistral 7B** | Excelente | Media | ⭐⭐⭐⭐ |
| **Llama 3.1 70B** | Excepcional | Muy lenta | ⭐⭐⭐⭐⭐ |
| **Claude 3.5 Sonnet** | Excepcional | N/A (API) | ⭐⭐⭐⭐⭐ |

## 💡 Workflows de Ejemplo

### Ejemplo 1: Corrección Simple con Ollama

```
Webhook (trabajo estudiante) → HTTP Request (Ollama) → Slack (resultado)
```

**Prompt para Ollama:**
```
Eres un profesor de secundaria. Corrige este trabajo considerando:
- Claridad de ideas
- Ortografía
- Estructura

Trabajo: {{ $json.trabajo }}

Proporciona:
1. Calificación (sobre 10)
2. 2 fortalezas
3. 2 áreas de mejora
4. Comentario general
```

### Ejemplo 2: Generación de Actividades

```
Formulario (tema, nivel) → HTTP Request (Ollama) → Google Docs
```

**Prompt:**
```
Crea una actividad educativa sobre {{ $json.tema }} para {{ $json.nivel }}.
Incluye:
- Objetivos de aprendizaje
- Materiales necesarios
- Desarrollo paso a paso (30 minutos)
- Criterios de evaluación
```

### Ejemplo 3: Análisis de Datos Simple

```
CSV → Code Node (extraer datos) → HTTP Request (Ollama) → Email
```

## 🎛️ Optimización

### Para Servidores sin GPU (CPU only)

1. **Usa modelos más pequeños** (7B-8B parámetros)
2. **Aumenta contexto gradualmente** - No envíes documentos enormes
3. **Divide tareas** - En lugar de una petición larga, haz varias cortas
4. **Configura n8n para esperar** - Aumenta timeout en HTTP Request node:
   - **Timeout**: 120000 ms (2 minutos) o más

### Para Servidores con GPU NVIDIA

Descomenta la sección `deploy` en el docker-compose:

```yaml
ollama:
  deploy:
    resources:
      reservations:
        devices:
          - driver: nvidia
            count: 1
            capabilities: [gpu]
```

Instala NVIDIA Container Toolkit primero:
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html

## 🔍 Comandos Útiles

```bash
# Ver logs de Ollama
docker-compose -f docker-compose-n8n-ollama.yml logs -f ollama

# Listar modelos descargados
docker exec ollama-ollama-1 ollama list

# Eliminar un modelo
docker exec ollama-ollama-1 ollama rm llama3.1

# Actualizar un modelo
docker exec ollama-ollama-1 ollama pull llama3.1:latest

# Ver información de un modelo
docker exec ollama-ollama-1 ollama show llama3.1

# Probar Ollama manualmente
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.1",
  "prompt": "Hola, ¿cómo estás?"
}'

# Ver uso de recursos
docker stats
```

## ❓ Troubleshooting

### Ollama tarda mucho en responder

**Solución:**
- Usa un modelo más pequeño
- Aumenta el timeout en n8n a 180 segundos
- Considera usar GPU

### "Model not found" error

**Solución:**
```bash
# Verifica que el modelo está descargado
docker exec ollama-ollama-1 ollama list

# Descarga el modelo si falta
docker exec ollama-ollama-1 ollama pull llama3.1
```

### Error de memoria (OOM)

**Solución:**
- Cierra otros servicios
- Usa un modelo más pequeño
- Aumenta swap del servidor
- Añade más RAM

### Puerto 11434 en uso

**Solución:**
```bash
# Cambia el puerto en docker-compose.yml
ports:
  - "11435:11434"  # Usa 11435 en tu host
```

## 📚 Recursos

- [Ollama Official](https://ollama.com/)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Modelos disponibles](https://ollama.com/library)
- [n8n Community Nodes](https://www.npmjs.com/search?q=n8n-nodes-ollama)

## 🤔 ¿Ollama o Claude API?

| Escenario | Recomendación |
|-----------|---------------|
| Presupuesto limitado | **Ollama** |
| Privacidad crítica (datos sensibles) | **Ollama** |
| Servidor potente (16GB+ RAM) | **Ollama** |
| Máxima calidad de IA | **Claude API** |
| Rapidez importante | **Claude API** |
| Sin GPU y poca RAM | **Claude API** |
| Conexión intermitente | **Ollama** |

**Híbrido:** Puedes tener ambos y usar Ollama para tareas simples y Claude para complejas.

---

**¿Necesitas ayuda descargando tu primer modelo?** ¡Dime y te guío paso a paso!
