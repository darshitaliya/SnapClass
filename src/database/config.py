import streamlit as st


from supabase import create_client, Client

# Use service_role key to bypass Row-Level Security for server-side operations.
# Never expose this key on the client side.
supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_SERVICE_KEY"]
)