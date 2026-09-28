#!/usr/bin/env python3
"""
🔒 RANSOMWARE DECRYPTOR
Sistema de descriptografia de arquivos para fins educacionais
"""

import os
import pyaes
from pathlib import Path

def decrypt_file(file_path, key):
    """Descriptografa um arquivo com AES-256-CTR"""
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"[!] Arquivo não encontrado: {file_path}")
        return None

    # Ler arquivo criptografado
    with open(file_path, "rb") as f:
        file_data = f.read()

    print(f"[*] Descriptografando: {file_path} ({len(file_data)} bytes)")

    try:
        # Descriptografar com AES-256-CTR
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover arquivo criptografado
        os.remove(file_path)

        # Salvar arquivo descriptografado
        decrypted_file = str(file_path).replace(".encrypted", "")
        with open(decrypted_file, "wb") as f:
            f.write(decrypt_data)

        print(f"[✓] Arquivo descriptografado: {decrypted_file}")
        return decrypted_file

    except Exception as e:
        print(f"[!] Erro ao descriptografar: {e}")
        return None


def decrypt_directory(dir_path, key):
    """Descriptografa todos os arquivos .encrypted de um diretório"""
    dir_path = Path(dir_path)

    if not dir_path.is_dir():
        print(f"[!] Diretório não encontrado: {dir_path}")
        return

    files = list(dir_path.rglob("*.encrypted"))

    if not files:
        print("[!] Nenhum arquivo .encrypted encontrado!")
        return

    print(f"\n[*] Descriptografando {len(files)} arquivo(s)...\n")

    count = 0
    for file_path in files:
        try:
            result = decrypt_file(file_path, key)
            if result:
                count += 1
        except Exception as e:
            print(f"[!] Erro ao descriptografar {file_path}: {e}")

    print(f"\n[✓] {count} arquivo(s) descriptografado(s)!")


def main():
    print("╔" + "═"*48 + "╗")
    print("║" + " "*10 + "🔒 RANSOMWARE DECRYPTOR 🔒" + " "*10 + "║")
    print("╚" + "═"*48 + "╝")

    while True:
        print("\n[MENU]")
        print("1. Descriptografar arquivo")
        print("2. Descriptografar diretório")
        print("3. Sair")

        choice = input("\n>>> Escolha uma opção: ").strip()

        if choice == "1":
            file_path = input(">>> Caminho do arquivo: ").strip()
            key = input(">>> Chave de descriptografia (32 caracteres): ").encode()

            if len(key) != 32:
                print("[!] Chave deve ter exatamente 32 caracteres (256 bits)!")
                continue

            decrypt_file(file_path, key)

        elif choice == "2":
            dir_path = input(">>> Caminho do diretório: ").strip()
            key = input(">>> Chave de descriptografia (32 caracteres): ").encode()

            if len(key) != 32:
                print("[!] Chave deve ter exatamente 32 caracteres (256 bits)!")
                continue

            decrypt_directory(dir_path, key)

        elif choice == "3":
            print("\n[*] Encerrando...")
            break

        else:
            print("[!] Opção inválida!")


if __name__ == "__main__":
    main()
