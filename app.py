import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors

st.set_page_config(page_title="IUPAC Name Generator", page_icon="🧪")
st.title("🧠 AI IUPAC Name Generator")

st.write("Upload a structure (in .mol, .sdf, or SMILES text) to get its IUPAC name.")

uploaded_file = st.file_uploader("Upload chemical structure file", type=["mol", "sdf", "txt"])

if uploaded_file is not None:
    file_bytes = uploaded_file.read().decode("utf-8")
    try:
        mol = Chem.MolFromMolBlock(file_bytes) or Chem.MolFromSmiles(file_bytes)
        if mol:
            name = Chem.MolToSmiles(mol)
            st.success(f"IUPAC/SMILES representation: {name}")
        else:
            st.error("❌ Could not read structure. Try another file.")
    except Exception as e:
        st.error(f"Error: {e}")

