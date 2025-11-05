# Filtros de Visão Computacional

Este projeto tem como objetivo demonstrar e analisar técnicas fundamentais de processamento digital de imagens com foco na detecção de bordas, esse estudo foi baseado no conteúdo sobre filtros do grupo de estudo sobre visão computacional do qual participo. A detecção de bordas é uma etapa indispensável para extração de informações estruturais de uma imagem e serve como base para sistemas mais avançados de visão computacional.

## Motivação

A identificação de bordas é amplamente utilizada em áreas como:

Sistemas de visão embarcados

Veículos autônomos e sistemas de direção assistida

Reconhecimento facial e autenticação biométrica

Processamento de imagens médicas (tomografia, ressonância, ultrassom)

Rastreamento e segmentação de objetos em vídeo

OCR (Reconhecimento Óptico de Caracteres)

Sistemas de inspeção industrial e metrologia

Este projeto reforça os conceitos essenciais para aplicações em aprendizado de máquina, visão computacional e inteligência artificial aplicada.

## Objetivos

Este trabalho busca:

Aplicar e comparar diferentes filtros de detecção de bordas

Analisar o comportamento de cada operador diante de diferentes características de imagem

Identificar vantagens e limitações de cada abordagem

Demonstrar, na prática, a diferença entre derivada contínua e derivada discreta

Explorar o uso de kernels convolucionais

Estabelecer uma base técnica para estágios posteriores de pré-processamento de imagens para IA

## Filtros Utilizados
### 1. Filtro de Sobel

O operador de Sobel utiliza derivadas discretas para calcular o gradiente de intensidade da imagem, destacando bordas horizontais e verticalmente.

Principais características:

Considera gradientes nas direções x e y

Realiza leve suavização contra ruído

Bom para encontrar contornos estruturais predominantes

### 2. Filtro Laplaciano

O operador Laplaciano aplica a segunda derivada da imagem, realçando variações abruptas de intensidade em qualquer direção.

Principais características:

Detecta bordas sem necessidade de orientação (omnidirecional)

Capta detalhes finos

Mais sensível ao ruído, podendo ser usado após suavização

### 3. Filtro Canny

O detector de Canny é um método multietapas considerado referência na literatura devido à sua robustez.

Principais características:

Suavização inicial utilizando filtro Gaussiano

Cálculo de gradiente (similar ao Sobel)

Supressão de não máximos

Histerese por limiar para definição final das bordas

Fornece bordas contínuas, limpas e com alta precisão

Derivada Contínua x Derivada Discreta
Conceito	Descrição
Derivada Contínua	Definida matematicamente para funções contínuas, representa taxa de variação instantânea
Derivada Discreta	Aproxima a derivada utilizando valores amostrais (pixels), aplicável a imagens digitais

Como as imagens são formadas por pixels, utilizamos aproximações de derivadas através de kernels convolucionais, responsáveis por detectar mudanças abruptas de intensidade entre regiões, caracterizando uma borda.

## Considerações Finais

Este projeto apresenta os principais operadores clássicos para detecção de bordas e estabelece fundamentos importantes para estudos avançados em visão computacional, incluindo redes neurais convolucionais, segmentação de imagens e rastreamento em vídeo.

Esse projeto foi criado baseado nas informações que obtive no grupo de estudo sobre visão computacional.
link que leva direto para o grupo no whattsapp: https://chat.whatsapp.com/G5lLNJdp9oxDb0fZVIT4ca?mode=ems_copy_c.

