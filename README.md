# 🔓 RANSOMWARE

Sistema educacional de criptografia de arquivos usando **AES-256-CTR**.

> ⚠️ **AVISO LEGAL**: Este projeto é para fins educacionais, de pesquisa de segurança e CTF (Capture The Flag) apenas. Uso indevido é ilegal.

---

## 📋 Índice

1. [Instalação](#-instalação)
2. [Uso Básico](#-uso-básico)
3. [Exemplos Práticos](#-exemplos-práticos)
4. [Estrutura do Projeto](#-estrutura-do-projeto)
5. [Testes](#-testes)

---

## 📦 Instalação

### Passo 1: Instale as dependências

```bash
pip install -r requirements.txt
```

Isso instalará:
- `pyaes==1.6.1` - Biblioteca de criptografia AES

### Passo 2: Verifique a instalação

```bash
python -c "import pyaes; print('✓ pyaes instalado com sucesso')"
```

---

## 🚀 Uso Básico

### Conceitos Importantes

- **Encrypter**: Criptografa seus arquivos
- **Decrypter**: Descriptografa seus arquivos
- **Chave**: 32 caracteres (256 bits) que protege seus dados
- **Arquivo Original**: Deletado após criptografar
- **Arquivo Criptografado**: Tem extensão `.encrypted`

### Sintaxe Geral

```
python encrypter.py     → Para criptografar
python decrypter.py     → Para descriptografar
```

---

## 📝 Uso Rápido

### 1️⃣ Criptografar Arquivo Único

```bash
python encrypter.py
```

Quando solicitar:
```
>>> Escolha uma opção: 1
>>> Caminho do arquivo: test_files/dados_secretos.txt
>>> Chave de criptografia (32 caracteres): SenhaForte1234567890123456789012
```

**Resultado**:
```
[*] Criptografando: test_files/dados_secretos.txt (563 bytes)
[✓] Arquivo criptografado: test_files/dados_secretos.txt.encrypted
```

### 2️⃣ Descriptografar Arquivo

```bash
python decrypter.py
```

Quando solicitar:
```
>>> Escolha uma opção: 1
>>> Caminho do arquivo: test_files/dados_secretos.txt.encrypted
>>> Chave de descriptografia (32 caracteres): SenhaForte1234567890123456789012
```

**Resultado**:
```
[*] Descriptografando: test_files/dados_secretos.txt.encrypted (563 bytes)
[✓] Arquivo descriptografado: test_files/dados_secretos.txt
```

### 3️⃣ Criptografar Diretório Inteiro

```bash
python encrypter.py
```

Quando solicitar:
```
>>> Escolha uma opção: 2
>>> Caminho do diretório: test_files/
>>> Chave de criptografia (32 caracteres): MinhaChave12345678901234567890ab
```

**Resultado**:
```
[*] Criptografando 3 arquivo(s)...

[*] Criptografando: test_files/arquivo1.txt (500 bytes)
[✓] Arquivo criptografado: test_files/arquivo1.txt.encrypted
[1/3] ✓

[✓] 3 arquivo(s) criptografado(s)!
```

### 4️⃣ Descriptografar Diretório

```bash
python decrypter.py
```

Quando solicitar:
```
>>> Escolha uma opção: 2
>>> Caminho do diretório: test_files/
>>> Chave de descriptografia (32 caracteres): MinhaChave12345678901234567890ab
```

---

## 📝 Exemplo Completo - Passo a Passo

### Arquivo de Teste

Temos um arquivo de teste pronto:
```
test_files/dados_secretos.txt
```

### Passo 1: Verifique o arquivo original

```bash
cat test_files/dados_secretos.txt
```

**Saída**:
```
════════════════════════════════════════════════════════════
               ARQUIVO SUPER SECRETO
════════════════════════════════════════════════════════════

INFORMAÇÕES CONFIDENCIAIS:
- Senha do Banco: SuperSenha@2024!
- API Token: ghp_1234567890abcdefghijklmnopqrst
...
```

### Passo 2: Criptografe

```bash
python encrypter.py
```

Menu:
```
╔════════════════════════════════════════════════╗
║        🔓 RANSOMWARE ENCRYPTOR 🔓            ║
╚════════════════════════════════════════════════╝

[MENU]
1. Criptografar arquivo
2. Criptografar diretório
3. Sair

>>> Escolha uma opção: 1
>>> Caminho do arquivo: test_files/dados_secretos.txt
>>> Chave de criptografia (32 caracteres): SenhaForte1234567890123456789012
```

**Saída**:
```
[*] Criptografando: test_files/dados_secretos.txt (563 bytes)
[✓] Arquivo criptografado: test_files/dados_secretos.txt.encrypted
```

### Passo 3: Verifique que foi criptografado

```bash
# Arquivo original não existe mais
ls -la test_files/dados_secretos.txt
# Erro: arquivo não encontrado ✓

# Arquivo criptografado existe
ls -la test_files/dados_secretos.txt.encrypted
# -rw-rw-r-- 1 vinicius vinicius 563 Sep 28 20:XX

# Conteúdo é ilegível
cat test_files/dados_secretos.txt.encrypted
# Mostra caracteres aleatórios/binários ✓
```

### Passo 4: Descriptografe

```bash
python decrypter.py
```

Menu:
```
╔════════════════════════════════════════════════╗
║        🔒 RANSOMWARE DECRYPTOR 🔒            ║
╚════════════════════════════════════════════════╝

[MENU]
1. Descriptografar arquivo
2. Descriptografar diretório
3. Sair

>>> Escolha uma opção: 1
>>> Caminho do arquivo: test_files/dados_secretos.txt.encrypted
>>> Chave de descriptografia (32 caracteres): SenhaForte1234567890123456789012
```

**Saída**:
```
[*] Descriptografando: test_files/dados_secretos.txt.encrypted (563 bytes)
[✓] Arquivo descriptografado: test_files/dados_secretos.txt
```

### Passo 5: Verifique a integridade

```bash
# Arquivo criptografado não existe mais
ls -la test_files/dados_secretos.txt.encrypted
# Erro: arquivo não encontrado ✓

# Arquivo original foi recuperado
ls -la test_files/dados_secretos.txt
# -rw-rw-r-- 1 vinicius vinicius 563 Sep 28 20:XX

# Conteúdo é idêntico ao original
cat test_files/dados_secretos.txt
# Mostra o conteúdo original ✓
```

## 🔐 Especificações Técnicas

- **Algoritmo**: AES-256-CTR (Advanced Encryption Standard)
- **Tamanho da Chave**: 256 bits (32 caracteres)
- **Modo**: CTR (Counter)
- **Biblioteca**: pyaes

## ⚠️ Importante

- **A chave DEVE ter exatamente 32 caracteres**
- O arquivo original é **DELETADO** após criptografar
- O arquivo criptografado é **DELETADO** após descriptografar
- **GUARDE SUA CHAVE COM SEGURANÇA**
- Sem a chave correta, não há como recuperar os dados

---

## 🧪 Testes

### Teste 1: Teste Automatizado (Recomendado)

```bash
python test_example.py
```

Verifica:
- ✓ Criptografia funciona
- ✓ Arquivo original é deletado
- ✓ Arquivo criptografado é ilegível
- ✓ Descriptografia funciona
- ✓ Conteúdo é idêntico ao original

**Resultado esperado**:
```
╔════════════════════════════════════════════════╗
║            TESTE DO RANSOMWARE                ║
╚════════════════════════════════════════════════╝

[1] Criptografando arquivo...
[*] Criptografando: teste.txt (38 bytes)
[✓] Arquivo criptografado: teste.txt.encrypted

[2] Verificando arquivo criptografado...
    Arquivo: teste.txt.encrypted
    Tamanho: 38 bytes
    Conteúdo (primeiros 30 bytes): b'\xf6\x98x\x8b\x1d...'

[3] Descriptografando arquivo...
[*] Descriptografando: teste.txt.encrypted (38 bytes)
[✓] Arquivo descriptografado: teste.txt

[4] Verificando integridade...
    ✓ Sucesso! Conteúdo idêntico ao original

╚════════════════════════════════════════════════╝
TESTE CONCLUÍDO COM SUCESSO!
```

### Teste 2: Teste Manual com test_files

```bash
# Passo 1: Criptografe
python encrypter.py
# Digite: 1
# Digite: test_files/dados_secretos.txt
# Digite: SenhaForte1234567890123456789012

# Passo 2: Verifique
ls -la test_files/
# Deve ver: dados_secretos.txt.encrypted (original deletado)

# Passo 3: Descriptografe
python decrypter.py
# Digite: 1
# Digite: test_files/dados_secretos.txt.encrypted
# Digite: SenhaForte1234567890123456789012

# Passo 4: Verifique
ls -la test_files/
# Deve ver: dados_secretos.txt (criptografado deletado)

# Passo 5: Compare
cat test_files/dados_secretos.txt
# Conteúdo deve ser idêntico ao original
```

### Teste 3: Teste com Chave Errada

```bash
# Criptografe com uma chave
python encrypter.py
# Chave: SenhaCorreta1234567890123456789

# Tente descriptografar com outra chave
python decrypter.py
# Chave: SenhaErrada9876543210987654321

# Resultado: Arquivo será corrompido/ilegível
```

---

## ⚠️ Troubleshooting

### Problema: "Chave deve ter 32 caracteres"

```bash
# Sua chave tem comprimento errado
# Conte: cada caractere = 1

SenhaForte1234567890123456789012
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 32 caracteres (CORRETO)

SenhaForte123456789012345678  
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^
 27 caracteres (ERRADO - faltam 5)
```

### Problema: "Arquivo não encontrado"

```bash
# Verifique o caminho
# Caminho pode ser:
# - Absoluto: /home/vinicius/Documents/cyber-security/test_files/dados_secretos.txt
# - Relativo: test_files/dados_secretos.txt

# Liste os arquivos
ls -la test_files/
```

### Problema: "Arquivo descriptografado está corrompido"

```bash
# Você usou a chave errada
# Verifique se usou a mesma chave em ambas operações

# Se perdeu a chave original:
# ❌ Arquivo é IRRECUPERÁVEL
# Sempre guarde a chave com segurança!
```

### Problema: "pyaes não está instalado"

```bash
# Instale as dependências
pip install -r requirements.txt

# Ou manualmente
pip install pyaes==1.6.1

# Verifique
python -c "import pyaes; print('OK')"
```

---

## 📊 Performance

Tempo de processamento por tamanho de arquivo:

| Tamanho | Tempo Estimado |
|---------|---|
| 1 KB | < 1ms |
| 100 KB | ~10ms |
| 1 MB | ~50ms |
| 10 MB | ~500ms |
| 100 MB | ~5s |
| 1 GB | ~50s |

---

## 🌐 Como Contribuir

Para adicionar ao GitHub:

```bash
# Iniciar repositório Git
git init

# Adicionar arquivos
git add encrypter.py decrypter.py test_example.py README.md requirements.txt .gitignore

# Fazer primeiro commit
git commit -m "feat: ransomware educacional com AES-256-CTR"

# Criar branch main
git branch -M main

# Adicionar repositório remoto
git remote add origin https://github.com/seu-usuario/ransomware.git

# Fazer push
git push -u origin main
```

---

## 📂 Estrutura do Projeto

```
ransomware/
│
├── 📄 encrypter.py              # Script para criptografar
├── 📄 decrypter.py              # Script para descriptografar
├── 📄 test_example.py           # Teste automatizado
├── 📄 README.md                 # Esta documentação
├── 📄 requirements.txt          # Dependências Python
├── 📄 .gitignore               # Arquivos ignorados no Git
│
└── 📁 test_files/              # Pasta com arquivos de teste
    └── 📄 dados_secretos.txt    # Arquivo de exemplo
```

### O que cada arquivo faz?

| Arquivo | Função |
|---------|--------|
| `encrypter.py` | Menu interativo para criptografar arquivos/diretórios |
| `decrypter.py` | Menu interativo para descriptografar arquivos/diretórios |
| `test_example.py` | Script automatizado que testa criptografia + descriptografia |
| `README.md` | Documentação completa (este arquivo) |
| `requirements.txt` | Lista de bibliotecas necessárias (`pyaes`) |
| `.gitignore` | Arquivos que o Git ignora (não faz commit) |
| `test_files/` | Pasta com arquivos de teste |
| `test_files/dados_secretos.txt` | Arquivo de exemplo para testar |

---

## 🔐 Segurança

### Especificações Técnicas

```
Algoritmo de Criptografia: AES-256-CTR
Tamanho da Chave: 256 bits (32 caracteres)
Modo de Operação: CTR (Counter)
Biblioteca: pyaes v1.6.1
```

### Importante Saber

1. **A chave DEVE ter exatamente 32 caracteres**
   ```bash
   # ✓ Correto: 32 caracteres
   SenhaForte1234567890123456789012
   
   # ✗ Errado: menos de 32
   SenhaForte123456789012345678
   
   # ✗ Errado: mais de 32
   SenhaForte12345678901234567890123
   ```

2. **Arquivo original é deletado após criptografar**
   ```bash
   # Antes:
   dados_secretos.txt       (500 bytes)
   
   # Depois:
   dados_secretos.txt.encrypted  (500 bytes)
   dados_secretos.txt            (DELETADO!)
   ```

3. **Arquivo criptografado é deletado após descriptografar**
   ```bash
   # Antes:
   dados_secretos.txt.encrypted  (500 bytes)
   
   # Depois:
   dados_secretos.txt            (500 bytes)
   dados_secretos.txt.encrypted  (DELETADO!)
   ```

4. **Sem a chave correta, dados são irrecuperáveis**
   ```bash
   # ✓ Certo: mesma chave usada
   Chave: SenhaForte1234567890123456789012
   Resultado: Arquivo descriptografado com sucesso
   
   # ✗ Errado: chave diferente
   Chave: OutraChave9876543210987654321098
   Resultado: Arquivo corrompido (IRRECUPERÁVEL)
   ```

### Dicas de Segurança

✅ **Use chaves únicas e fortes**
```
Bom:  ABCdefgh123456!@#$%7890abcdefgh
Ruim: 12345678901234567890123456789012
Ruim: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

✅ **Guarde a chave em local seguro**
- Não coloque em código
- Não compartilhe por email
- Use gerenciador de senhas

✅ **Faça backup da chave**
- Se perder a chave, dados são irrecuperáveis
- Guarde em múltiplos locais seguros

❌ **NÃO use chaves óbvias**
- Datas: 20262926092826092800
- Sequências: 12345678901234567890123456789012
- Padrões: aaaabbbbccccddddeeeeffffffff

## 📊 Performance

- **Arquivo 1 MB**: ~50ms
- **Arquivo 10 MB**: ~500ms
- **Arquivo 100 MB**: ~5s
- **Diretório 1GB**: ~50s


---

## 📚 Referências

- [pyaes - GitHub](https://github.com/ricmoo/pyaes)
- [AES Encryption - Wikipedia](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [CTR Mode - Wikipedia](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR))
- [Cryptography Best Practices - OWASP](https://owasp.org/)

---

## ⚖️ Disclaimer Legal

Este projeto é fornecido **APENAS para fins educacionais e de pesquisa**.

### ✓ Uso Permitido

- ✓ Use em ambientes controlados
- ✓ Use para aprender sobre criptografia
- ✓ Use em CTF competitions
- ✓ Use para proteger seus próprios dados
- ✓ Use em pesquisa acadêmica
- ✓ Use em cursos de segurança

### ✗ Uso Proibido

- ✗ NÃO use para prejudicar terceiros
- ✗ NÃO use para extorsão ou chantagem
- ✗ NÃO use contra vontade de outros
- ✗ NÃO use para atividades ilegais
- ✗ NÃO use para roubo de dados
- ✗ NÃO use para sabotagem

**Uso indevido é CRIME e sujeito a penalidades legais severas.**

---

## 📞 Suporte Rápido

```bash
# Para testar se tudo funciona
python test_example.py

# Para ver o menu interativo
python encrypter.py
python decrypter.py

# Para verificar a instalação
pip list | grep pyaes
```

---

**Desenvolvido para fins educacionais - 2026** 🔒

*Use com responsabilidade!*
