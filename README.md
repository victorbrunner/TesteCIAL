# TesteCIAL
Script para Teste Tecnico - CIAL

Instruções gerais:

O objetivo do RPA é capturar todos os possíveis balanços dentro do site específico de publicidade legal. Para isso é necessário: - Entrar no site (https://publilegal.diariodenoticias.com.br/)

- Filtrar por balanços em Seção

- Obter da tabela abaixo os dados (Razão Social, título, data, seção e link do balanço) e gravar em uma tabela Excel em um arquivo separado

- É esperado que o resultado final em Excel seja parecido com este:

OBS 1: É importante ressaltar que para o preenchimento/classificação da coluna “Tipo” do exemplo acima, devem ser considerar todos como “Balanços”.

OBS 2: A Coluna CNPJ deve ser populada com o CNPJ extraído do PDF de cada Balanço, e se possível formatar no padrão “00.000.000/0001-00”.

OBS3: A tabela em excel deve possuir o nome padrão “Extract_ {today_date}.xlsx”

Recomendações para o desenvolvimento

- Utilizar a biblioteca Playwright para interação com os elementos do Chrome

- Utilizar a biblioteca Requests para extração do CNPJ dentro do PDF de cada balanço
