# 📂 File Organizer CLI

Script em Python para organizar automaticamente arquivos de uma pasta por categoria (Imagens, Documentos, Planilhas, Vídeos, Áudios, Compactados e Outros).

Ideal para limpar pastas como Downloads de forma rápida e segura.

## Recursos

- **Zero dependências externas:** Roda nativamente com Python 3.8+.
- **Modo Dry-Run:** Permite simular as alterações antes de mover os arquivos de fato.
- **Tratamento de Colisão:** Preserva arquivos existentes adicionando sufixos numéricos (`_1`, `_2`) em caso de nomes duplicados na pasta de destino.
- **Seguro:** Ignora diretórios e processa apenas arquivos da raiz indicada (não recursivo).

## Como Usar

Copie e cole o comando referente ao seu caso de uso:

```bash
# 1. Organizar a pasta atual onde o terminal está aberto
python organizer.py

# 2. Organizar uma pasta específica (caminho absoluto ou relativo)
python organizer.py ~/Downloads
python organizer.py /caminho/para/pasta

# 3. Simular a organização sem mover nada (Dry-run) na pasta atual ou específica
python organizer.py --dry-run
python organizer.py ~/Downloads --dry-run