import streamlit as st
from hindsight_client import Hindsight

st.set_page_config(
    page_title="MemorySupport",
    page_icon="🧠"
)

st.title("🧠 MemorySupport")
st.subheader("AI Customer Support Agent")

st.write(
    "A customer support agent that remembers previous conversations."
)

client = Hindsight(
    base_url="http://localhost:8888"
)

customer = st.text_input("Customer Name")
message = st.text_area("Enter your message")

if st.button("Send"):

    if not customer or not message:
        st.warning("Please enter customer name and message.")

    else:
        bank_id = (
            "customer-" +
            customer.strip().lower().replace(" ", "-")
        )

        # Create memory bank
        try:
            client.create_bank(
                bank_id=bank_id,
                name=f"{customer} Support Memory"
            )
        except Exception:
            pass

        # Recall previous memories BEFORE saving new message
        memories = client.recall(
            bank_id=bank_id,
            query=message
        )

        st.subheader("🧠 Customer Memory")

        if memories.results:
            for memory in memories.results[:5]:
                st.write("• " + memory.text)
        else:
            st.info("No previous memory found.")

        # Save current conversation
        client.retain(
            bank_id=bank_id,
            content=f"Customer {customer} said: {message}",
            context="Customer support conversation"
        )

        st.subheader("🤖 Support Agent")

        if memories.results:
            st.write(
                f"Hi {customer}! I remember your previous conversation. "
                "I can use that information to better understand your "
                "current issue and continue helping you."
            )
        else:
            st.write(
                f"Hi {customer}! Thanks for contacting us. "
                "I've saved this conversation so I can remember it "
                "for future support."
            )
