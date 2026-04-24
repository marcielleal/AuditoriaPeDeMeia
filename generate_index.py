import os

# Nome do arquivo de saída
output_file = "index.html"

# Extensão que queremos buscar
extension = ".html"

def generate_html():
    files = [f for f in os.listdir('.') if f.endswith(extension) and f != output_file]
    files.sort()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("<html>\n<head><title>Índice de Projetos</title></head>\n<body>\n")
        f.write("<h1>Lista de Arquivos HTML</h1>\n<ul>\n")
        
        for file in files:
            f.write(f'  <li><a href="{file}">{file}</a></li>\n')
            
        f.write("</ul>\n</body>\n</html>")

if __name__ == "__main__":
    generate_index()
