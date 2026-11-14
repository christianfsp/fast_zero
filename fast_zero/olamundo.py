# ruff: noqa: E501
def ola_mundo():
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Olá, mundo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --fundo: #14122b;
      --texto: #f5f3ff;
      --suave: #a9a3d6;
      --azul: #4f8cff;
      --rosa: #ff5fa2;
      --amarelo: #ffd166;
    }

    * { box-sizing: border-box; margin: 0; }

    html, body { height: 100%; }

    body {
      display: grid;
      place-items: center;
      background: var(--fundo);
      color: var(--texto);
      font-family: "Figtree", system-ui, sans-serif;
      overflow: hidden;
      padding: 1.5rem;
    }

    /* Três esferas de luz ao fundo */
    .luz {
      position: fixed;
      width: 42vmax;
      height: 42vmax;
      border-radius: 50%;
      filter: blur(90px);
      opacity: .45;
      z-index: 0;
    }
    .luz.a { background: var(--azul);    top: -15vmax; left: -12vmax; }
    .luz.b { background: var(--rosa);    bottom: -18vmax; right: -10vmax; }
    .luz.c { background: var(--amarelo); width: 22vmax; height: 22vmax; top: 55%; left: 8%; opacity: .25; }

    main {
      position: relative;
      z-index: 1;
      text-align: center;
      padding: clamp(2rem, 6vw, 4rem) clamp(1.5rem, 8vw, 5rem);
      border-radius: 28px;
      background: rgba(255, 255, 255, .06);
      border: 1px solid rgba(255, 255, 255, .14);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      box-shadow: 0 30px 80px rgba(0, 0, 0, .35);
      animation: entrada .9s cubic-bezier(.2, .7, .2, 1) both;
    }

    h1 {
      font-family: "Bricolage Grotesque", system-ui, sans-serif;
      font-weight: 800;
      font-size: clamp(3rem, 12vw, 8rem);
      line-height: .95;
      letter-spacing: -.03em;
      background: linear-gradient(100deg, var(--azul), var(--rosa), var(--amarelo), var(--azul));
      background-size: 250% 100%;
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      animation: brilho 8s linear infinite;
    }

    p {
      margin-top: 1.25rem;
      font-size: clamp(1rem, 2.4vw, 1.25rem);
      color: var(--suave);
    }

    a.botao {
      display: inline-block;
      margin-top: 2rem;
      padding: .85rem 1.8rem;
      border-radius: 999px;
      background: var(--texto);
      color: var(--fundo);
      font-weight: 500;
      text-decoration: none;
      transition: transform .2s ease, box-shadow .2s ease;
    }
    a.botao:hover { transform: translateY(-3px); box-shadow: 0 10px 28px rgba(255, 95, 162, .45); }
    a.botao:focus-visible { outline: 3px solid var(--amarelo); outline-offset: 3px; }

    @keyframes entrada {
      from { opacity: 0; transform: translateY(24px) scale(.97); }
      to   { opacity: 1; transform: none; }
    }
    @keyframes brilho {
      to { background-position: 250% 0; }
    }

    @media (prefers-reduced-motion: reduce) {
      main, h1 { animation: none; }
      a.botao { transition: none; }
    }
  </style>
</head>
<body>
  <div class="luz a"></div>
  <div class="luz b"></div>
  <div class="luz c"></div>

  <main>
    <h1>Olá,<br>mundo!</h1>
    <p>Minha primeira página, feita com HTML e CSS.</p>
    <a class="botao" href="#" onclick="alert('Olá, mundo!'); return false;">Dizer olá</a>
  </main>
</body>
</html>
 """
