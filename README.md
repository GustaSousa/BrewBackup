# Guia de Uso para Script de Instalação de Aplicativos Homebrew

Este guia descreve como usar o script Python para instalar aplicativos do Homebrew listados em um arquivo de backup.

## Requisitos

1. **Python 3.x**: Certifique-se de que o Python 3 está instalado em seu sistema.
2. **Homebrew**: Certifique-se de que o Homebrew está instalado e configurado corretamente.

## Preparação

### Criar o Arquivo `brew_backup.txt`

Abra o terminal e crie o arquivo `brew_backup.txt` na área de trabalho com a lista dos aplicativos que deseja instalar:

1. **Abra o Terminal**:
   - No macOS, você pode abrir o Terminal procurando por "Terminal" no Spotlight ou acessando `/Applications/Utilities/Terminal`.
   - No Linux, você pode abrir o Terminal procurando por "Terminal" no menu de aplicativos ou usando o atalho `Ctrl+Alt+T`.


2. **Gere o arquivo install_brew_apps.sh com o seguinte script:**

    ```bash 
    #!/bin/bash

    # Cria um arquivo chamado brew_backup.txt na pasta home do usuário
    brew list > ~/brew_backup.txt

    # Mensagem de sucesso
    echo "Lista de aplicativos Homebrew instalada salva em ~/brew_backup.txt"

## Uso

### 1. Navegue até o Diretório do Script

Abra um terminal e navegue até o diretório onde o arquivo `install_brew_apps.py` está localizado. Por exemplo:

       cd /caminho/para/seu/script/

### 2. Execute o Script

Execute o script Python para iniciar a instalação dos aplicativos listados no arquivo `brew_backup.txt`:

    python3 install_brew_apps.py

### 3. Verifique a Instalação

O script lerá o arquivo `brew_backup.txt` e instalará cada aplicativo listado usando o **Homebrew**. Verifique o terminal para ver o progresso e quaisquer mensagens de erro que possam aparecer.
