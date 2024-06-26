import subprocess

def install_brew_apps(file_path):
    try:
        with open(file_path, 'r') as file:
            packages = file.readlines()
        
        for package in packages:
            package = package.strip()
            if package:
                print(f"Instalando {package}...")
                result = subprocess.run(['brew', 'install', package], capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"{package} instalado com sucesso.")
                else:
                    print(f"Erro ao instalar {package}: {result.stderr}")
        
        print("Instalação completa dos aplicativos do Homebrew.")
    
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado. Certifique-se de que o arquivo está no diretório correto.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    file_path = '~/brew_backup.txt'
    # Expande o caminho do arquivo
    expanded_file_path = subprocess.run(['bash', '-c', f'echo {file_path}'], capture_output=True, text=True).stdout.strip()
    install_brew_apps(expanded_file_path)