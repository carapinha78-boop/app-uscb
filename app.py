import streamlit as st
from datetime import datetime

# Configuração de Identidade Visual (Cores da CGTP/USCB)
st.set_page_config(page_title="USCB - União de Sindicatos", page_icon="⚖️")

# Estilo para botões vermelhos
st.markdown("""
    <style>
    .stButton>button { background-color: #d32f2f; color: white; border-radius: 5px; }
    .stTextInput>div>div>input { border-color: #d32f2f; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ União de Sindicatos de Castelo Branco")
st.subheader("Portal do Trabalhador")

menu = st.sidebar.radio("Navegação", ["Início/Notícias", "Documentos PDF", "Registo / Sindicalização"])

# --- RODAPÉ RGPD ---
st.sidebar.markdown("---")
st.sidebar.caption("📧 **Contacto Oficial:**")
st.sidebar.caption("uscb.cgtp@gmail.com")

# --- INÍCIO / NOTÍCIAS ---
if menu == "Início/Notícias":
    st.header("🗞️ Atualidade Sindical")
    st.info("Consulte aqui os últimos comunicados da USCB/CGTP-IN.")
    
    with st.expander("📢 Bem-vindo ao novo Portal"):
        st.write("Este portal foi criado para aproximar a USCB dos trabalhadores de Castelo Branco. Aqui pode consultar documentos e solicitar apoio.")

# --- DOCUMENTOS PDF ---
elif menu == "Documentos PDF":
    st.header("📄 Biblioteca de Documentos")
    st.write("Clique abaixo para ler ou descarregar os documentos oficiais.")
    
    # Exemplo de PDF (Substitua o link quando tiver o seu)
    pdf_url = "https://www.w3.org"
    
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("⬇️ Descarregar PDF", pdf_url)
    
    st.divider()
    st.pdf(pdf_url)

# --- FORMULÁRIO (Envia para o seu Email) ---
elif menu == "Registo / Sindicalização":
    st.header("📝 Formulário de Contacto e Registo")
    st.write("Preencha os dados abaixo. A informação será enviada de forma segura para a USCB.")

    # Usamos o FormSubmit para enviar os dados para o seu email sem precisar de base de dados
    contact_form = f"""
    <form action="https://formsubmit.co" method="POST">
        <input type="hidden" name="_subject" value="Novo Registo na App USCB">
        <input type="text" name="nome" placeholder="Seu Nome Completo" required style="width:100%; margin-bottom:10px; padding:10px;">
        <input type="email" name="email" placeholder="Seu Email" required style="width:100%; margin-bottom:10px; padding:10px;">
        <input type="text" name="empresa" placeholder="Empresa / Local de Trabalho" required style="width:100%; margin-bottom:10px; padding:10px;">
        <select name="sindicalizado" style="width:100%; margin-bottom:10px; padding:10px;">
            <option value="nao">Não sou sindicalizado</option>
            <option value="sim">Já sou sindicalizado</option>
        </select>
        <p style="font-size: 12px;">Ao enviar, aceita que a USCB trate os seus dados de acordo com o RGPD.</p>
        <button type="submit" style="background-color: #d32f2f; color: white; padding: 10px 20px; border: none; cursor: pointer; width: 100%;">ENVIAR DADOS</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
