import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]: %(message)s')

PROJECT_NAME = 'lgpd_rag'

# ESTRUTURA CORRIGIDA E MELHORADA
list_of_files = [
    # === NOTEBOOKS ===
    f'notebooks/{PROJECT_NAME}_prototype.ipynb',
    f'notebooks/data_exploration.ipynb',
    f'notebooks/model_evaluation.ipynb',
    
    # === CÓDIGO FONTE PRINCIPAL ===
    f'src/__init__.py',
    f'src/config.py',
    f'src/loader.py',
    f'src/splitter.py',
    f'src/embedder.py',
    f'src/vectorstore.py',
    f'src/retriever.py',
       
    # === APLICAÇÃO ===
    f'app/__init__.py',
    f'app/app.py',
    f'app/front_end/__init__.py',
    f'app/front_end/app.py',
    f'app/front_end/components.py',
    f'app/front_end/static/style.css',
    f'app/front_end/templates/index.html',
    f'app/back_end/__init__.py',
    f'app/back_end/app.py',
    f'app/back_end/api.py',
    f'app/back_end/routes.py',
    f'app/back_end/models.py',
    
    # === TESTES ===
    f'tests/__init__.py',
    f'tests/test_loader.py',
    f'tests/test_splitter.py',
    f'tests/test_embedder.py',
    f'tests/test_vectorstore.py',
    f'tests/test_retriever.py',
    f'tests/test_api.py',
    f'tests/conftest.py',
    
    # === DADOS ===
    f'data/raw/.gitkeep',
    f'data/processed/.gitkeep',
    f'data/vectorstore/.gitkeep',
    f'data/documents/.gitkeep',
    
    # === SCRIPTS ===
    f'scripts/prepare_data.py',
    f'scripts/get_data.py',
    f'scripts/train_embeddings.py',
    f'scripts/evaluate_model.py',
    f'scripts/deploy.py',
    
    # === CONFIGURAÇÃO E DEPLOYMENT ===
    f'config/development.yaml',
    f'config/production.yaml',
    f'config/logging.yaml',
    
    # === DOCKER E CI/CD ===
    f'Dockerfile',
    f'docker-compose.yml',
    f'.github/workflows/ci.yml',
    f'.github/workflows/deploy.yml',
    
    # === DOCUMENTAÇÃO ===
    f'README.md',
    f'docs/INSTALLATION.md',
    f'docs/API_REFERENCE.md',
    f'docs/CONTRIBUTING.md',
    f'docs/DEPLOYMENT.md',
    f'docs/ARCHITECTURE.md',
    
    # === ARQUIVOS DE CONFIGURAÇÃO ===
    f'requirements.txt',
    f'requirements-dev.txt',
    f'pyproject.toml',
    f'.env.example',
    f'.env',
    f'.gitignore',
    f'.pre-commit-config.yaml',
    f'pytest.ini',
    f'setup.py',
]

def create_project_structure():
    """Cria a estrutura de pastas melhorada"""
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)
        
        # Criar diretório se não existir
        if filedir != '':
            os.makedirs(filedir, exist_ok=True)
            logging.info(f'Creating directory {filedir} for the file {filename}')
        
        # Criar arquivo se não existir ou estiver vazio
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, 'w') as f:
                # Adicionar conteúdo básico dependendo do tipo de arquivo
                if filename.endswith('.py'):
                    if filename == '__init__.py':
                        f.write('"""Package initialization file."""\n')
                    else:
                        f.write(f'"""{filename} module."""\n\n')
                elif filename.endswith('.md'):
                    f.write(f'# {filename.replace(".md", "").replace("_", " ").title()}\n\n')
                elif filename == '.gitignore':
                    f.write(get_gitignore_content())
                elif filename == 'requirements.txt':
                    f.write(get_requirements_content())
                elif filename.endswith('.yaml') or filename.endswith('.yml'):
                    f.write('# Configuration file\n')
                
            logging.info(f'Creating empty file: {filepath}')
        else:
            logging.info(f'{filename} already exists')

def get_gitignore_content():
    """Retorna conteúdo padrão para .gitignore"""
    return """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific
.env
*.log
data/raw/*
data/processed/*
data/vectorstore/*
!data/*/.gitkeep

# Jupyter Notebooks
.ipynb_checkpoints

# Docker
.dockerignore

# Testing
.pytest_cache/
.coverage
htmlcov/

# Models and large files
*.pkl
*.joblib
*.h5
*.model
"""

def get_requirements_content():
    """Retorna conteúdo padrão para requirements.txt"""
    return """# Core RAG Dependencies
langchain>=0.1.0
langchain-community>=0.0.20
langchain-openai>=0.0.8
langchain-huggingface>=0.0.3

# Vector Store
faiss-cpu>=1.7.4
chromadb>=0.4.0

# Document Processing
pypdf>=4.0.0
python-docx>=0.8.11
unstructured>=0.12.0

# Embeddings
sentence-transformers>=2.2.2
transformers>=4.35.0

# Web Framework
fastapi>=0.104.0
streamlit>=1.28.0
uvicorn>=0.24.0

# Data Processing
pandas>=2.1.0
numpy>=1.24.0

# Environment
python-dotenv>=1.0.0
pydantic>=2.5.0
pydantic-settings>=2.1.0

# Monitoring and Logging
loguru>=0.7.0
wandb>=0.16.0

# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
httpx>=0.25.0

# Development
black>=23.0.0
isort>=5.12.0
flake8>=6.0.0
pre-commit>=3.5.0
"""

# Função principal para executar
if __name__ == "__main__":
    print("🚀 Criando estrutura melhorada do projeto RAG LGPD...")
    create_project_structure()
    print("✅ Estrutura do projeto criada com sucesso!")
    
    print(f"\n📁 Estrutura criada em: ./{PROJECT_NAME}/")
    print("\n🔧 Próximos passos:")
    print("1. cd lgpd_rag")
    print("2. python -m venv venv")
    print("3. source venv/bin/activate  # Linux/Mac")
    print("   # ou venv\\Scripts\\activate  # Windows")
    print("4. pip install -r requirements.txt")
    print("5. cp .env.example .env")
    print("6. # Configure suas variáveis de ambiente no .env")
    print("7. python -m pytest tests/")