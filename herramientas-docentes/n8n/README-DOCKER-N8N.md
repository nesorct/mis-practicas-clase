# 🐳 n8n + Claude API - Docker Compose Setup

Configuración completa de n8n con integración a Claude API (Anthropic) usando Docker Compose.

## 📋 Características

- ✅ **n8n** - Plataforma de automatización de workflows
- ✅ **PostgreSQL** - Base de datos para producción (más robusto que SQLite)
- ✅ **Redis** - Colas de ejecución para workflows pesados con IA
- ✅ **Claude API** - Integración lista con Anthropic
- ✅ **Volumen persistente** - Compatible con tu volumen Docker existente
- ✅ **Seguridad** - Autenticación y encriptación configuradas

## 🚀 Instalación Rápida

### Paso 1: Clonar/Descargar Archivos

Descarga estos archivos en tu servidor:
- `docker-compose-n8n-claude.yml`
- `.env.example`
- `redis.conf`

### Paso 2: Configurar Variables de Entorno

```bash
# Copia el archivo de ejemplo
cp .env.example .env

# Edita el archivo con tu editor favorito
nano .env  # o vim, o code
```

**Variables obligatorias a modificar:**

```env
# Seguridad - ¡Cambia estas!
N8N_ENCRYPTION_KEY=openssl rand -hex 32  # Genera una clave
N8N_BASIC_AUTH_PASSWORD=tu_contraseña_segura

# API Key de Claude (obténla en https://console.anthropic.com/)
ANTHROPIC_API_KEY=sk-ant-xxxxx

# Si tienes un volumen existente, pon su nombre aquí
N8N_VOLUME=tu_volumen_existente
```

### Paso 3: Generar Clave de Encriptación

```bash
# Genera una clave segura de 64 caracteres hex
openssl rand -hex 32

# Copia el resultado y pégalo en N8N_ENCRYPTION_KEY en el .env
```

### Paso 4: Iniciar Servicios

```bash
# Opción A: Si NO tienes un volumen existente
docker-compose -f docker-compose-n8n-claude.yml up -d

# Opción B: Si tienes un volumen existente
# Edita el .env primero y pon el nombre de tu volumen en N8N_VOLUME
docker-compose -f docker-compose-n8n-claude.yml up -d
```

### Paso 5: Verificar Instalación

```bash
# Ver logs
docker-compose -f docker-compose-n8n-claude.yml logs -f n8n

# Verificar que está corriendo
docker ps

# Acceder a n8n
# http://localhost:5678 (o la IP de tu servidor)
```

## 🔧 Configuración de Claude en n8n

### Método 1: HTTP Request Node (Recomendado para empezar)

1. Crea un nuevo workflow en n8n
2. Añade un nodo **HTTP Request**
3. Configura:
   - **Method**: POST
   - **URL**: `https://api.anthropic.com/v1/messages`
   - **Headers**:
     - `x-api-key`: `${ANTHROPIC_API_KEY}` (o tu API key directamente)
     - `anthropic-version`: `2023-06-01`
     - `Content-Type`: `application/json`
   - **Body**:
   ```json
   {
     "model": "claude-3-5-sonnet-20241022",
     "max_tokens": 1024,
     "messages": [
       {"role": "user", "content": "Hola Claude, analiza esto: {{ $json.input }}"}
     ]
   }
   ```

### Método 2: AI Agent Node (Avanzado)

1. Crea un workflow
2. Añade nodo **AI Agent**
3. Conecta un nodo **Anthropic Chat Model**
4. Configura tu API key en las credenciales

### Método 3: Credential Vault (Más seguro)

1. En n8n, ve a **Settings → Credentials**
2. Clic en **Add Credential**
3. Selecciona **Anthropic**
4. Pega tu API key
5. Guarda y usa en cualquier nodo

## 📁 Estructura de Archivos

```
.
├── docker-compose-n8n-claude.yml    # Configuración principal
├── .env                               # Variables de entorno (NO subir a Git!)
├── .env.example                       # Plantilla de variables
├── redis.conf                         # Configuración de Redis
├── n8n-local-files/                   # Archivos locales (se crea automáticamente)
└── README.md                          # Este archivo
```

## 🔌 Workflows de Ejemplo

### Ejemplo 1: Webhook → Claude → Respuesta

```
Webhook Trigger → HTTP Request (Claude) → Code Node → Respond to Webhook
```

**Webhook URL:** `POST http://tu-servidor:5678/webhook/claude-analisis`

### Ejemplo 2: Email → Claude procesa → Guarda en Google Sheets

```
Email Trigger → Extract Attachment → Claude analiza → Google Sheets
```

### Ejemplo 3: Schedule → Claude genera contenido → Publica en Slack

```
Schedule Trigger → Claude genera resumen → Slack Message
```

## 🛠️ Comandos Útiles

```bash
# Iniciar servicios
docker-compose -f docker-compose-n8n-claude.yml up -d

# Ver logs
docker-compose -f docker-compose-n8n-claude.yml logs -f n8n
docker-compose -f docker-compose-n8n-claude.yml logs -f postgres
docker-compose -f docker-compose-n8n-claude.yml logs -f redis

# Detener servicios
docker-compose -f docker-compose-n8n-claude.yml down

# Detener y eliminar volúmenes (¡CUIDADO!)
docker-compose -f docker-compose-n8n-claude.yml down -v

# Reiniciar un servicio
docker-compose -f docker-compose-n8n-claude.yml restart n8n

# Escalar workers (si está habilitado)
docker-compose -f docker-compose-n8n-claude.yml up -d --scale n8n-worker=3

# Entrar al contenedor de n8n
docker exec -it n8n-n8n-1 /bin/sh

# Backup de PostgreSQL
docker exec n8n-postgres-1 pg_dump -U n8n n8n > backup_$(date +%F).sql

# Ver espacio de volúmenes
docker system df -v
```

## 🔒 Seguridad

### Protección del archivo .env

El archivo `.env` **NO debe subirse a GitHub**. Ya está incluido en `.gitignore`.

### Buenas prácticas:

1. **Usa contraseñas fuertes** para `N8N_BASIC_AUTH_PASSWORD` y `POSTGRES_PASSWORD`
2. **Genera una `N8N_ENCRYPTION_KEY` única** y guárdala en un lugar seguro
3. **Nunca commitees la API key** de Anthropic
4. **Usa HTTPS** en producción (con Traefik, Nginx, o Caddy)
5. **Restringe el acceso** al puerto 5678 solo a IPs confiables

### Generar API Key de Anthropic:

1. Ve a https://console.anthropic.com/
2. Crea cuenta o inicia sesión
3. Ve a **"API Keys"** → **"Create Key"**
4. Copia la clave (empieza con `sk-ant-`)
5. Pégala en tu archivo `.env` en `ANTHROPIC_API_KEY`

## 💰 Costos

### n8n
- **Self-hosted**: Gratis (tú gestionas el servidor)
- **n8n Cloud**: Desde $20/mes

### Anthropic Claude API
- **Precio por token**: ~$3/millón de tokens de entrada
- **Claude 3.5 Sonnet**: Buen balance precio/rendimiento
- **Claude 3 Haiku**: Más barato, para tareas simples
- **Claude 3 Opus**: Más caro, para tareas complejas

### Servidor (si usas VPS)
- **Mínimo recomendado**: 2 CPU, 4GB RAM, 20GB SSD
- **Ejemplo**: DigitalOcean Droplet $24/mes, AWS t3.medium, etc.

## 🔧 Troubleshooting

### Problema: n8n no inicia

```bash
# Ver logs
docker-compose logs n8n

# Posibles causas:
# 1. PostgreSQL no está listo (deja que el healthcheck pase)
# 2. Falta N8N_ENCRYPTION_KEY
# 3. Permisos de volúmenes
```

### Problema: Error de conexión a PostgreSQL

```bash
# Verificar que postgres está corriendo
docker ps | grep postgres

# Reiniciar servicios
docker-compose -f docker-compose-n8n-claude.yml restart postgres n8n
```

### Problema: API Key no funciona

```bash
# Verificar que está en el .env
cat .env | grep ANTHROPIC_API_KEY

# Probar la API key con curl
curl -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 100,
    "messages": [{"role": "user", "content": "Hola"}]
  }'
```

### Problema: Volumen existente no se monta

```bash
# Listar volúmenes Docker
docker volume ls

# Verificar nombre en .env
# Debe coincidir exactamente: N8N_VOLUME=nombre_exacto_del_volumen
```

## 📚 Recursos

- [Documentación n8n Docker](https://docs.n8n.io/hosting/installation/docker/)
- [Documentación Anthropic API](https://docs.anthropic.com/)
- [n8n Claude Integrations](https://n8n.io/integrations/claude/)
- [Community Forum n8n](https://community.n8n.io/)

## 🤝 Contribuir

Si mejoras este setup, ¡comparte los cambios!

## 📄 Licencia

MIT License - Usa libremente para fines personales o comerciales.

---

**¿Preguntas?** Abre un issue en GitHub o contacta al autor.
