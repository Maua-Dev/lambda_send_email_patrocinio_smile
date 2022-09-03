def generate_html(
  company_name, 
  colab_name, 
  cnpj,
  sponsor_type, 
  closure_date, 
  email, 
  number
  ):
    return f"""
    <html>
      <head></head>
      <body>
        <h3>Mais uma empresa deseja entrar no grupo de patrocinadores da SMILE</h3>
        <p>Segue abaixo as principais informações e contato:
        </p>
        <ul>
        	<li><strong>Nome da empresa: </strong> {company_name}</li>
            <li><strong>Nome do colaborador(a): </strong> {colab_name}</li>
            <li><strong>CNPJ: </strong> {cnpj}</li>
            <li><strong>Cota de patrocínio: {sponsor_type}</strong></li>
            <li><strong>Período de fechamento: </strong> {closure_date}</li>
            <li><strong>E-mail: </strong> {email}</li>
            <li><strong>Telefone: </strong> {number}</li>
        </ul>
      </body>
    </html>
    """