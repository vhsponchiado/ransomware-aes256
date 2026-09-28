#!/usr/bin/env python3
"""
Teste do RANSOMWARE - Encriptor e Decryptor
"""

from encrypter import encrypt_file
from decrypter import decrypt_file
from pathlib import Path

# Chave de teste (32 caracteres = 256 bits)
KEY = b"chavedeteste12345678901234567890"

# Criar arquivo de teste
test_file = Path("teste.txt")
test_file.write_text("ARQUIVO CRIPTOGRAFADO PELO RANSOMWARE!")

print("╔" + "═"*48 + "╗")
print("║" + " "*12 + "TESTE DO RANSOMWARE" + " "*16 + "║")
print("╚" + "═"*48 + "╝")

# 1. Criptografar
print("\n[1] Criptografando arquivo...")
encrypted = encrypt_file(test_file, KEY)

# 2. Verificar que foi criptografado
print("\n[2] Verificando arquivo criptografado...")
encrypted_path = Path(encrypted)
encrypted_content = encrypted_path.read_bytes()
print(f"    Arquivo: {encrypted}")
print(f"    Tamanho: {len(encrypted_content)} bytes")
print(f"    Conteúdo (primeiros 30 bytes): {encrypted_content[:30]}")

# 3. Descriptografar
print("\n[3] Descriptografando arquivo...")
decrypted = decrypt_file(encrypted_path, KEY)

# 4. Verificar integridade
print("\n[4] Verificando integridade...")
original_content = "ARQUIVO CRIPTOGRAFADO PELO RANSOMWARE!"
decrypted_content = Path(decrypted).read_text()

if original_content == decrypted_content:
    print(f"    ✓ Sucesso! Conteúdo idêntico ao original")
    print(f"    Conteúdo: '{decrypted_content}'")
else:
    print(f"    ✗ Erro! Conteúdo diferente")

print("\n" + "╚" + "═"*48 + "╝")
print("TESTE CONCLUÍDO COM SUCESSO!")
print("╚" + "═"*48 + "╝")
