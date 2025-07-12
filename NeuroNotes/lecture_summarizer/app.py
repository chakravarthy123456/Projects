import streamlit as st
from summarizer import get_transcript_text, summarize_text

st.set_page_config(page_title="🎓 YouTube Lecture Summarizer")

st.title("🎓 YouTube Lecture Summarizer Tool")
st.markdown("Summarize any YouTube lecture in seconds using AI (powered by Hugging Face)!")

video_url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Summary"):
    if not video_url:
        st.warning("Please enter a YouTube video URL.")
    else:
        with st.spinner("Fetching transcript..."):
            transcript_text = get_transcript_text(video_url)
        
        if transcript_text:
            st.success("Transcript fetched successfully!")
            with st.spinner("Generating summary..."):
                summary = summarize_text(transcript_text)
            st.subheader("📘 Summary")
            st.write(summary)
        else:
            st.error("Could not fetch transcript for this video. It may not have captions.")
