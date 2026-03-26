import gradio as gr

# HTML da página de apresentação dos livros
html_page = """
<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8" />
  <title>Livros de Renato Alves</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body {
  font-family: Arial, sans-serif;
  margin: 0;
  background: #0066CC;
  color: #1a1a1a; /* texto mais escuro */
}

header {
  background: linear-gradient(135deg, #1e40af, #15803d);
  color: #ffffff;
  padding: 2rem 1rem;
  text-align: center;
}

.tag {
  font-size: 1.0rem;
  font-weight: bold;
  background: #0066CC; /* mais escuro */
  color: #0f2f8a;      /* azul mais forte */
  padding: 0.2rem 0.6rem;
  border-radius: 20px;
  display: inline-block;
  margin-bottom: 0.4rem;
}

.book-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin: 0.3rem 0;
  color: #111; /* mais escuro */
}

.meta {
  font-size: 0.85rem;
  color: #333; /* mais escuro */
  line-height: 1.4;
}

.synopsis {
  margin-top: 0.5rem;
  font-size: 0.9rem;
  line-height: 1.5;
  color: #222; /* mais escuro */
}

.btn {
  display: inline-block;
  margin-top: 0.8rem;
  padding: 0.5rem 1rem;
  background: #c7dbff; /* igual ao azul do header */
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  transition: 0.2s;
}
.btn:hover {
  background: #16348A; /* hover coerente */
}


footer {
  text-align: center;
  padding: 2rem 1rem;
  font-size: 0.8rem;
  color: #555; /* mais escuro */
}

  </style>
</head>

<body>

<header>
  <h1>Livros de Renato Alves</h1>
  <p>Descobre histórias cheias de aventura, imaginação e mistério.</p>
</header>

<main>
  <section class="grid">

    <!-- O Cruzeiro dos Animais -->
    <article class="book-card">
      <img class="book-cover"
           src="https://www.atlanticbookshop.pt/storage/app/media/imageresizecache/18f/003/187/18f003187963074d232953c75c24395da55230cc30d204b0c2815a9f9f6178c3.jpg"
           alt="Capa do livro O Cruzeiro dos Animais">
      <div class="book-body">
        <span class="tag">7 aos 10 anos</span>
        <h2 class="book-title">O Cruzeiro dos Animais</h2>

        <p class="meta">
          Editora: Flamingo Edições<br>
          Publicado em: 25/10/2021<br>
          Páginas: 44<br>
          ISBN: 978-989-37-2067-7
        </p>

        <p class="synopsis">
          Acompanha a Gi, o Rafa, a Hippo, o Potter, a Elle e o Fant num cruzeiro
          que passa pela Madeira, Portimão, Lisboa, Açores e Porto, numa aventura
          divertida que dá a conhecer Portugal aos mais novos.
        </p>

        <a class="btn"
           href="https://www.atlanticbookshop.pt/7-aos-10-anos/o-cruzeiro-dos-animais"
           target="_blank">Comprar na Atlantic Bookshop</a>
      </div>
    </article>
<br>
    <!-- A Magia dos Livros -->
    <article class="book-card">
      <img class="book-cover"
           src="https://www.atlanticbookshop.pt/storage/app/media/imageresizecache/987/f1c/b12/987f1cb127934a9cffb8221568c93273fa110ff0ee6e82b7c7400dcb43ef40dc.jpg"
           alt="Capa do livro A Magia dos Livros">
      <div class="book-body">
        <span class="tag">7 aos 10 anos</span>
        <h2 class="book-title">A Magia dos Livros</h2>

        <p class="meta">
          Editora: Flamingo Edições<br>
          Publicado em: 16/11/2022<br>
          Páginas: 52<br>
          ISBN: 978-989-37-4498-7
        </p>

        <p class="synopsis">
          Alexandre, de oito anos, passa férias com o primo Tiago, de dez. Entre
          futebol, brincadeiras e uma misteriosa mansão abandonada, descobrem
          segredos que revelam o verdadeiro poder dos livros.
        </p>

        <a class="btn"
           href="https://www.atlanticbookshop.pt/7-aos-10-anos/a-magia-dos-livros"
           target="_blank">Comprar na Atlantic Bookshop</a>
      </div>
    </article>
<br>
    <!-- A Viagem de Carro dos Animais -->
    <article class="book-card">
      <img class="book-cover"
           src="https://img.wook.pt/images/a-viagem-de-carro-dos-animais-renato-alves/MXwyOTQ0MjkxMHwyNTg0OTYyOXwxNzcyOTAwMTE2MDAwfHdlYnA=/500x"
           alt="Capa do livro A Viagem de Carro dos Animais">
      <div class="book-body">
        <span class="tag">Infanto-juvenil</span>
        <h2 class="book-title">A Viagem de Carro dos Animais</h2>

        <p class="meta">
          Editora: Flamingo Edições<br>
          Publicado em: 24/10/2023<br>
          Páginas: 66<br>
          ISBN: 978-989-37-6561-6
        </p>

        <p class="synopsis">
          Junta-te à Gi, ao Rafa, à Hippo, ao Potter, à Elle, ao Fant e à Fanty
          numa viagem de carro por Portugal, cheia de descobertas, monumentos
          icónicos e aventuras inesquecíveis.
        </p>

        <a class="btn"
           href="https://www.atlanticbookshop.pt/infanto-juvenis/a-viagem-de-carro-dos-animais"
           target="_blank">Comprar na Atlantic Bookshop</a>
      </div>
    </article>
<br>
    <!-- A Tartaruga Madruga -->
    <article class="book-card">
      <img class="book-cover"
           src="https://img.wook.pt/images/a-tartaruga-madruga-renato-alves/MXwzMzI4MTg1NXwyOTczNzM2OXwxNzc0MDA0ODU5MDAwfHdlYnA=/500x"
           alt="Capa do livro A Tartaruga Madruga">
      <div class="book-body">
        <span class="tag">Infanto-juvenil</span>
        <h2 class="book-title">A Tartaruga Madruga</h2>

        <p class="meta">
          Editora: Oficina da Escrita<br>
          Preço: 12,00 €
        </p>

        <p class="synopsis">
          Madruga, uma tartaruga cheia de energia, vive no aquário do Simão.
          Quando o seu brinquedo favorito desaparece, ela e o gato Félix iniciam
          uma investigação divertida e cheia de mistério.
        </p>

        <a class="btn"
           href="https://oficinadaescrita.com/produto/a-tartaruga-madruga/"
           target="_blank">Comprar na Oficina da Escrita</a>
      </div>
    </article>
<br>
  </section>
</main>

<footer>
  Página informativa baseada nos dados públicos das editoras e livrarias.
</footer>

</body>
</html>
"""

# Interface Gradio
with gr.Blocks(title="Livros de Renato Alves") as demo:
    gr.HTML(html_page)

demo.launch()