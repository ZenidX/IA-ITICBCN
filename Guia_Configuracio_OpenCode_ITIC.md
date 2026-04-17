# Guia de Configuracio d'OpenCode amb Ollama - ITIC Barcelona

**Data:** Marc 2026
**Autor:** Equip IA - ITIC Barcelona
**Versio:** 1.0

---

## Que es OpenCode?

OpenCode es una eina CLI (Command Line Interface) de codi obert per a assistencia de programacio amb IA. Funciona de manera similar a altres assistents de codi, pero amb l'avantatge de poder connectar-se a models locals via Ollama o a diversos proveidors cloud.

**Caracteristiques principals:**
- Interficie de terminal interactiva
- Suport per a multiples proveidors d'IA (Ollama, OpenAI, Anthropic, etc.)
- Capacitats agentiques (lectura/escriptura de fitxers, execucio de comandes)
- Integracio amb MCP (Model Context Protocol)
- Sessions persistents i exportables

---

## Requisits previs

### Sistema operatiu
- Windows 10/11, macOS o Linux

### Programari necessari
- **Node.js** versio 18 o superior
- **Git** (recomanat)
- Connexio a la xarxa interna de l'ITIC (per accedir al servidor Ollama)

### Verificar Node.js
```bash
node --version
# Ha de mostrar v18.x.x o superior
```

---

## 1. Installacio d'OpenCode

### Windows (PowerShell com a Administrador)
```powershell
# Opcio A: Via npm (recomanat)
npm install -g opencode-ai

# Opcio B: Installacio directa
irm https://opencode.ai/install.ps1 | iex
```

### macOS / Linux
```bash
# Opcio A: Via npm (recomanat)
npm install -g opencode-ai

# Opcio B: Installacio directa
curl -fsSL https://opencode.ai/install.sh | bash
```

### Verificar la installacio
```bash
opencode --version
# Ha de mostrar: 1.4.8 o superior
```

---

## 2. Configuracio per al servidor Ollama de l'ITIC

### Dades de connexio del servidor

| Servei | URL |
|--------|-----|
| **API Ollama** | `http://192.168.1.22:11434` |
| **Open WebUI** | `http://192.168.1.22:8080` |

### Models disponibles al servidor

| Model | Parametres | Quantitzacio | Mida | Us recomanat |
|-------|------------|--------------|------|--------------|
| **gpt-oss:120b** | 116.8B | MXFP4 | ~65 GB | Tasques complexes, RAG, raonament |
| **qwen3.5:35b** | 36.0B | Q4_K_M | ~24 GB | Equilibri qualitat/velocitat |
| **Qwen3-Coder-30B** | 30.5B | Q6_K | ~26 GB | Generacio i revisio de codi |
| **gemma3:270m** | 268M | Q8_0 | ~291 MB | Proves rapides, prototipat |

---

## 3. Crear el fitxer de configuracio

### Pas 3.1: Crear el directori de configuracio

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.config\opencode"
```

**macOS / Linux:**
```bash
mkdir -p ~/.config/opencode
```

### Pas 3.2: Crear el fitxer de configuracio

Crea el fitxer `opencode.json` al directori de configuracio:

**Windows:** `%USERPROFILE%\.config\opencode\opencode.json`
**macOS/Linux:** `~/.config/opencode/opencode.json`

> **IMPORTANT - Models futurs**
>
> Els models disponibles al servidor aniran canviant amb el temps. Quan s'afegeixin
> nous models, haureu d'actualitzar aquest fitxer manualment per poder utilitzar-los.
>
> **Com saber quins models hi ha disponibles?**
> ```bash
> curl http://192.168.1.22:11434/api/tags
> ```
>
> **Com afegir un nou model?** Afegeix una entrada dins de `"models": { }` amb el format:
> ```json
> "nom-del-model:tag": {
>   "name": "Nom descriptiu",
>   "tools": true
> }
> ```
>
> El nom del model ha de coincidir exactament amb el que retorna la comanda anterior.

### Contingut del fitxer de configuracio

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama-itic": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama ITIC Barcelona",
      "options": {
        "baseURL": "http://192.168.1.22:11434/v1"
      },
      "models": {
        "gpt-oss:120b": {
          "name": "GPT-OSS 120B (Principal)",
          "tools": true
        },
        "qwen3.5:35b": {
          "name": "Qwen 3.5 35B (Rapid)",
          "tools": true
        },
        "danielsheep/Qwen3-Coder-30B-A3B-Instruct-1M-Unsloth:UD-Q6_K_XL": {
          "name": "Qwen3 Coder 30B",
          "tools": true
        },
        "gemma3:270m": {
          "name": "Gemma 3 270M (Test)",
          "tools": true
        }
      }
    }
  }
}
```

### Pas 3.3: Crear el fitxer amb PowerShell (Windows)

Copia i enganxa aquesta comanda:

```powershell
@'
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama-itic": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama ITIC Barcelona",
      "options": {
        "baseURL": "http://192.168.1.22:11434/v1"
      },
      "models": {
        "gpt-oss:120b": {
          "name": "GPT-OSS 120B (Principal)",
          "tools": true
        },
        "qwen3.5:35b": {
          "name": "Qwen 3.5 35B (Rapid)",
          "tools": true
        },
        "danielsheep/Qwen3-Coder-30B-A3B-Instruct-1M-Unsloth:UD-Q6_K_XL": {
          "name": "Qwen3 Coder 30B",
          "tools": true
        },
        "gemma3:270m": {
          "name": "Gemma 3 270M (Test)",
          "tools": true
        }
      }
    }
  }
}
'@ | Out-File -FilePath "$env:USERPROFILE\.config\opencode\opencode.json" -Encoding UTF8
```

---

## 4. Verificar la configuracio

### Comprovar connexio al servidor
```bash
curl http://192.168.1.22:11434/api/tags
```

Ha de retornar una llista JSON amb els models disponibles.

### Llistar proveidors configurats
```bash
opencode providers list
```

Ha de mostrar "Ollama ITIC Barcelona" com a proveidor disponible.

### Llistar models disponibles
```bash
opencode models ollama-itic
```

---

## 5. Utilitzar OpenCode

### Iniciar OpenCode amb el model per defecte
```bash
opencode
```

### Iniciar amb un model especific
```bash
# Model principal (120B) - maxima qualitat
opencode -m ollama-itic/gpt-oss:120b

# Model rapid (35B) - bon equilibri
opencode -m ollama-itic/qwen3.5:35b

# Model de codi (30B) - especialitzat en programacio
opencode -m "ollama-itic/danielsheep/Qwen3-Coder-30B-A3B-Instruct-1M-Unsloth:UD-Q6_K_XL"

# Model lleuger (270M) - proves rapides
opencode -m ollama-itic/gemma3:270m
```

### Iniciar en un projecte especific
```bash
opencode /ruta/al/teu/projecte
```

### Continuar l'ultima sessio
```bash
opencode --continue
```

---

## 6. Comandes utils dins d'OpenCode

Un cop dins de la interficie d'OpenCode:

| Comanda | Descripcio |
|---------|------------|
| `/help` | Mostra l'ajuda |
| `/model` | Canvia de model |
| `/clear` | Neteja la conversa |
| `/save` | Guarda la sessio |
| `/exit` o `Ctrl+C` | Surt d'OpenCode |

---

## 7. Resolucio de problemes

### Error: "Connection refused"
- Verifica que estas connectat a la xarxa interna de l'ITIC
- Comprova que el servidor Ollama esta funcionant: `curl http://192.168.1.22:11434`

### Error: "Model not found"
- Llista els models disponibles: `curl http://192.168.1.22:11434/api/tags`
- Verifica que el nom del model es correcte a la configuracio

### Les eines (tools) no funcionen
El context window del model pot ser massa petit. Si tens acces al servidor, pots augmentar-lo:
```bash
# Al servidor Ollama
ollama run qwen3.5:35b
>>> /set parameter num_ctx 32768
>>> /save qwen3.5:35b-32k
>>> /bye
```

### OpenCode va lent
- Utilitza un model mes petit per proves (`gemma3:270m`)
- El model de 120B requereix mes temps de processament

---

## 8. Integracio amb projectes

### Exemple: Utilitzar OpenCode per a un projecte Python
```bash
cd /ruta/projecte-python
opencode -m ollama-itic/qwen3.5:35b
```

Dins d'OpenCode pots demanar:
- "Analitza l'estructura d'aquest projecte"
- "Crea una funcio per validar emails"
- "Explica que fa el fitxer main.py"
- "Afegeix tests unitaris per a utils.py"

### Exemple: Utilitzar OpenCode per revisar codi
```bash
opencode -m "ollama-itic/danielsheep/Qwen3-Coder-30B-A3B-Instruct-1M-Unsloth:UD-Q6_K_XL"
```

---

## Recursos addicionals

- **Documentacio oficial OpenCode:** https://opencode.ai/docs/
- **Configuracio de proveidors:** https://opencode.ai/docs/providers/
- **Open WebUI (interficie web):** http://192.168.1.22:8080
- **Guia Ollama + OpenCode:** https://docs.ollama.com/integrations/opencode

---

## Suport

Per a dubtes o problemes amb la configuracio, contacta amb:

- **Xavi Lara Moreno** - xavi.lara@iticbcn.cat
- **Equip CEIABD** - Institut TIC de Barcelona

---

*Aquesta infraestructura es fruit de la collaboracio amb Isard (info@isardvdi.com)*
