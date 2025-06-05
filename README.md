# 2025-1-A3-UDWMJ-FAPA-05
## Projeto A3
Aplicativo em Django com o tema 'Biblioteca'.

## Diagrama de Classes
```mermaid
classDiagram
  class Autor {
    -nome: String
    -idade: int
  }

  class Editora {
    -nome: String
    -anoFundacao: int
  }

  class Categoria {
    -nome: String
    -descricao: String
  }

  class Cliente {
    -nome: String
    -sobrenome: String
    -email: Email
    -celular: String
    -endereco: String
    -genero: "Masculino" | "Feminino" | "Outro"
  }

  class Livro {
    -titulo: String
    -Autor: Autor
    -Categoria: Categoria
    -Editora: Editora
    -anoPublicacao: int
  }

  class LivroCategoria {
    -livro: Livro
    -categoria: Categoria
  }

  class Emprestimo {
    -Cliente: Cliente
    -Bibliotecario: Bibliotecario
    -status: "em andamento", "finalizado"
    -dataInicio: Date
    -dataFim: Date
  }

  class ItemEmprestimo {
    -Livro: Livro
    -Emprestimo: Emprestimo
  }

  class Bibliotecario {
    -nome: String
    -sobrenome: String
    -turno: "Matutino" | "Vespertino"
  }

  Categoria o--> LivroCategoria : ManyToMany
  LivroCategoria o--> Livro : ManyToMany
  Autor "1" o--> "*" Livro
  Editora "1" o--> "*" Livro
  Cliente "1" o--> "*" Emprestimo
  Livro "1" o--> "*" ItemEmprestimo
  Emprestimo "1" o--> "*" ItemEmprestimo
  Bibliotecario "1" o--> "*" Emprestimo
