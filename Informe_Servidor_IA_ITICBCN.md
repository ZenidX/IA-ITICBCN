# Servidor d'IA disponible per a Projectes - ITIC Barcelona

**Data:** Març 2026
**De:** Xavi Lara Moreno
**Per a:** Equip de Projectes ITIC

---

## Ja tenim el servidor operatiu!

Companys,

Us escric per informar-vos que **ja tenim accés al servidor d'IA** que vam anunciar fa unes setmanes gràcies a la col·laboració amb Isard. El servidor està operatiu i llest per ser utilitzat als vostres projectes.

---

## Què hi ha disponible?

### Interfície Web: Open WebUI
- **URL:** http://192.168.1.22:8080
- Interfície gràfica intuïtiva per interactuar amb els models
- Historial de converses
- Gestió de models

### API Ollama (per integració en projectes)
- **URL:** http://192.168.1.22:11434
- Compatible amb l'estàndard OpenAI API
- Ideal per integrar amb: n8n, LangChain, aplicacions pròpies, RAG pipelines

---

## Models disponibles ara mateix

| Model | Paràmetres | Quantització | Mida | Cas d'ús recomanat |
|-------|------------|--------------|------|-------------------|
| **gpt-oss:120b** | 116.8B | MXFP4 | ~65 GB | Model principal per tasques complexes, RAG avançat, raonament |
| **qwen3.5:35b** | 36.0B | Q4_K_M | ~24 GB | Equilibri qualitat/velocitat, ús general |
| **Qwen3-Coder-30B** | 30.5B | Q6_K | ~26 GB | Generació i revisió de codi, documentació tècnica |
| **gemma3:270m** | 268M | Q8_0 | ~291 MB | Proves ràpides, prototipat, tasques lleugeres |

---

## Com utilitzar-ho als vostres projectes?

### 1. Accés directe via navegador
Simplement accediu a **http://192.168.1.22:8080** i podreu xatejar amb els models.

### 2. Integració via API (exemple cURL)
```bash
curl http://192.168.1.22:11434/api/generate -d '{
  "model": "gpt-oss:120b",
  "prompt": "Explica la formulació del sulfat de coure",
  "stream": false
}'
```

### 3. Integració amb Python
```python
import requests

response = requests.post('http://192.168.1.22:11434/api/generate', json={
    'model': 'gpt-oss:120b',
    'prompt': 'El teu prompt aquí',
    'stream': False
})
print(response.json()['response'])
```

### 4. Compatible amb OpenAI SDK
```python
from openai import OpenAI

client = OpenAI(
    base_url='http://192.168.1.22:11434/v1',
    api_key='ollama'  # Ollama no requereix API key real
)

response = client.chat.completions.create(
    model='gpt-oss:120b',
    messages=[{'role': 'user', 'content': 'Hola!'}]
)
```

---

## Projectes que poden beneficiar-se immediatament

Basant-nos en els projectes que tenim en marxa:

| Projecte | Aplicació del servidor |
|----------|----------------------|
| **QuimicAI** | RAG amb el model de 120B per respostes precises sobre formulació química |
| **AgendaTIC/Kiosk** | Processament de dades d'analytics amb LLM |
| **GreenIOT** | Anàlisi de sèries temporals i prediccions |
| **AirGen/Meteo** | Interpretació de dades meteorològiques |
| **Kronos** | OCR i classificació amb suport de LLM |
| **Projectes CEIABD** | Entrenament i fine-tuning de models NLP |

---

## Recomanacions d'ús

1. **Comenceu amb gemma3:270m** per proves ràpides i validar la connexió
2. **Utilitzeu gpt-oss:120b** per tasques de producció i qualitat màxima
3. **Qwen3-Coder** és ideal per projectes que involucren generació de codi

---

---

## OpenCode - Assistent de codi per terminal

Per a una experiència més avançada de programació amb IA, podeu utilitzar **OpenCode**, una eina CLI que connecta directament amb el servidor Ollama.

### Instal·lació ràpida
```bash
npm install -g opencode
```

### Configuració
Consulteu la guia completa: **Guia_Configuracio_OpenCode_ITIC.md**

### Ús bàsic
```bash
# Iniciar amb el model principal
opencode -m ollama-itic/gpt-oss:120b

# Model ràpid per tasques generals
opencode -m ollama-itic/qwen3.5:35b

# Model especialitzat en codi
opencode -m "ollama-itic/danielsheep/Qwen3-Coder-30B-A3B-Instruct-1M-Unsloth:UD-Q6_K_XL"
```

---

## Suport i contacte

Si teniu dubtes sobre com integrar el servidor als vostres projectes, contacteu amb mi o amb l'equip del CEIABD.

Recordeu que aquesta infraestructura és fruit de la col·laboració amb **Isard** (info@isardvdi.com), i els casos d'èxit que generem seran beneficiosos per ambdues parts.

---

*A tope, equip!*

**Xavi Lara Moreno**
Professor IA i tutor ASIX
Institut TIC de Barcelona
xavi.lara@iticbcn.cat
