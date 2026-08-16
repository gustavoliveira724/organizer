# File Organizer CLI

Utilitário em Python para organização automática de diretórios com base em extensões de arquivo.

## Recursos

- **Zero dependências externas:** Roda nativamente com Python 3.8+.
- **Modo Dry-Run:** Permite simular as alterações antes de mover os arquivos de fato.
- **Tratamento de Colisão:** Preserva arquivos existentes adicionando sufixos numéricos (`_1`, `_2`) em caso de nomes duplicados na pasta de destino.
- **Seguro:** Ignora diretórios e processa apenas arquivos da raiz indicada (não recursivo).

## Como Usar

### 1. Organizar o diretório atual
```bash
python organizer.py