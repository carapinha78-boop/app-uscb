import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração e Identidade
st.set_page_config(page_title="União de Sindicatos de Castelo Branco", page_icon="⚖️")
st.title("⚖️ União de Sindicatos de Castelo Branco")

# Menu de Navegação
menu = st.sidebar.radio("Navegação", ["Início/Notícias", "Documentos PDF", "Área de Membro", "Quero Sindicalizar-me"])

# --- RODAPÉ RGPD (Visível em todas as páginas) ---
st.sidebar.markdown("---")
st.sidebar.caption("📧 **Contacto RGPD:**")
st.sidebar.caption("uscb.cgtp@gmail.com")
st.sidebar.info("Os seus dados são tratados com sigilo profissional e segurança.")

# --- INÍCIO / NOTÍCIAS ---
if menu == "Início/Notícias":
    st.header("🗞️ Atualidade Sindical")
    st.write("Bem-vindo ao portal oficial da USCB/CGTP-IN.")
    # Exemplo de notícia com data
    st.info(f"📅 **{datetime.now().strftime('%d/%b/%Y')}** - Novo comunicado disponível na área de documentos.")

# --- PDF ---
elif menu == "Documentos PDF":
    st.header("📄 Documentos e Comunicados")
    # Para carregar PDFs, coloque o ficheiro no GitHub e use o link direto aqui
    st.warning("Selecione o documento abaixo para ler:")
    st.pdf("https://www.w3.org")

# --- REGISTO (Com conformidade legal) ---
elif menu == "Área de Membro":
    st.header("👤 Registo de Trabalhador")
    with st.form("registo_uscb"):
        nome = st.text_input("Nome Completo")
        email = st.text_input("Endereço de Email")
        empresa = st.text_input("Empresa/Local de Trabalho")
        sindicalizado = st.radio("Já é sindicalizado?", ["Sim", "Não"])
        sindicato_qual = st.text_input("Se sim, em que sindicato?")
        
        st.markdown("---")
        st.markdown("**Cláusula de Proteção de Dados (RGPD):**")
        st.write(f"Ao submeter, autoriza a USCB a tratar os seus dados para fins de apoio e informação sindical. Pode solicitar a retificação ou eliminação através de: **uscb.cgtp@gmail.com**.")
        
        consentimento = st.checkbox("Aceito os termos e condições de proteção de dados.")
        
        if st.form_submit_button("Submeter Registo"):
            if consentimento and nome and email:
                st.success("Dados enviados com sucesso! A USCB analisará o seu registo.")
                # Aqui os dados seriam enviados para a sua Google Sheet
            else:
                st.error("É necessário aceitar o consentimento e preencher os dados obrigatórios.")

# --- SINDICALIZAR-ME ---
elif menu == "Quero Sindicalizar-me":
    st.header("✊ Fortaleça a sua Voz")
    st.write("A sindicalização é a sua melhor defesa. Preencha os campos para recebermos o seu pedido.")
    with st.form("form_sind"):
        st.text_input("Contacto Telefónico")
        st.text_area("Dúvidas ou Questões")
        if st.form_submit_button("Enviar Pedido de Inscrição"):
            st.success("Obrigado pela sua confiança. Entraremos em contacto brevemente.")
