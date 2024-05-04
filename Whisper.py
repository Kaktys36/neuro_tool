from tempfile import NamedTemporaryFile
import whisper
import streamlit as st

class Transcription:
    def __init__(self, source: list):
        self.source = source
        self.audios = []

        for file in self.source:
            with NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
                tmp_file.write(file.getvalue())
                self.audios.append(tmp_file.name)

    def transcribe(
        self,
        whisper_model: str,
        translation: bool,
    ):

        # get whisper model
        transcriber = whisper.load_model(whisper_model)

        self.output = []

        for idx, _ in enumerate(self.audios):

            # identify language
            audio = whisper.load_audio(self.audios[idx])
            audio = whisper.pad_or_trim(audio)
            mel = whisper.log_mel_spectrogram(audio).to(transcriber.device)
            _, probs = transcriber.detect_language(mel)
            language = max(probs, key=probs.get)

            self.raw_output = transcriber.transcribe(
                self.audios[idx],
                language=language,
                verbose=True,
                word_timestamps=True
            )
            if(translation):
                self.translation = transcriber.transcribe(
                    self.audios[idx],
                    language=language,
                    verbose=True,
                    word_timestamps=True,
                    task='translate'
                )["text"]
                self.raw_output["translation"] = self.translation
            self.segments = self.raw_output["segments"]
            for segment in self.raw_output["segments"]:
                del segment["tokens"]
            self.raw_output.update(
                name=self.source[idx].name, language=language)
            self.output.append(self.raw_output)
            print(self.output)
            
with st.sidebar.form("input_form"):
    input_files = st.file_uploader(
        "Files", type=["mp4", "m4a", "mp3", "wav"], accept_multiple_files=True)

    whisper_model = st.selectbox("Whisper model", options=[
        "tiny", "base", "small", "medium", "large"], index=4)

    pauses = st.checkbox("Pausen transkribieren", value=False)

    translation = st.checkbox("Englische Übersetzung", value=False)

    transcribe = st.form_submit_button(label="Start")

if transcribe:
    if input_files:
        st.session_state.transcription = Transcription(
            input_files)
        st.session_state.transcription.transcribe(
            whisper_model, translation
        )
    else:
        st.error("Bitte wählen Sie eine Datei")

# if there is a transcription, render it. If not, display instructions
if "transcription" in st.session_state:

    for i, output in enumerate(st.session_state.transcription.output):
        doc = docx.Document()
        avg_confidence_score = 0
        amount_words = 0
        save_dir = str(pathlib.Path(__file__).parent.absolute()
                       ) + "/transcripts/"
        st.markdown(
            f"#### Transkription von {output['name']}")
        for idx, segment in enumerate(output['segments']):
            for w in output['segments'][idx]['words']:
                amount_words += 1
                avg_confidence_score += w['probability']
        st.markdown(
            f"_(whisper model:_`{whisper_model}` -  _language:_ `{output['language']}` -  _⌀ confidence score:_ `{round(avg_confidence_score / amount_words,3)}`)")
        prev_word_end = -1
        text = ""
        html_text = ""
        # Define the color map
        colors = [(0.6, 0, 0), (1, 0.7, 0), (0, 0.6, 0)]
        cmap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)

        with st.expander("Transkript"):
            color_coding = st.checkbox(
                "Farbkodierung", value=False, key={i}, help='Farbkodierung eines Wortes auf der Grundlage der Wahrscheinlichkeit, dass es richtig erkannt wurde. Die Farbskala reicht von grün (hoch) bis rot (niedrig).')
            for idx, segment in enumerate(output['segments']):
                for w in output['segments'][idx]['words']:
                    # check for pauses in speech longer than 3s
                    if pauses and prev_word_end != -1 and w['start'] - prev_word_end >= 3:
                        pause = w['start'] - prev_word_end
                        pause_int = int(pause)
                        html_text += f'{"."*pause_int}{{{pause_int}sek}}'
                        text += f'{"."*pause_int}{{{pause_int}sek}}'
                    prev_word_end = w['end']
                    if (color_coding):
                        rgba_color = cmap(w['probability'])
                        rgb_color = tuple(round(x * 255)
                                          for x in rgba_color[:3])
                    else:
                        rgb_color = (0, 0, 0)
                    html_text += f"<span style='color:rgb{rgb_color}'>{w['word']}</span>"
                    text += w['word']
                    # insert line break if there is a punctuation mark
                    if any(c in w['word'] for c in "!?.") and not any(c.isdigit() for c in w['word']):
                        html_text += "<br><br>"
                        text += '\n\n'
            st.markdown(html_text, unsafe_allow_html=True)
            doc.add_paragraph(text)

        if (translation):
            with st.expander("Englische Übersetzung"):
                st.markdown(output["translation"], unsafe_allow_html=True)

        # save transcript as docx. in local folder
        file_name = output['name'] + "-" + whisper_model + \
            "-" + datetime.today().strftime('%d-%m-%y') + ".docx"
        doc.save(save_dir + file_name)

        bio = io.BytesIO()
        doc.save(bio)
        st.download_button(
            label="Download Transkript",
            data=bio.getvalue(),
            file_name=file_name,
            mime="docx"
        )

else:
    # show instruction page
    st.markdown("<h1>WHISPER - AUTOMATISCHE TRANSKRIPTION </h1> <p> Dieses Projekt wurde im Rahmen der Masterarbeit von <a href='mailto:johanna.jaeger89@icloud.com'> Johanna Jäger<a/> " +
                "unter der Verwendung von <a href='https://openai.com/blog/whisper'> OpenAI Whisper</a> durchgeführt.</p> <h2 class='highlight'>DATENSCHUTZ: </h2> <p>Das Programm wird lokal ausgeführt. " +
                "Die Transkripte werden in ein lokales Verzeichnis dieses PCs gespeichert. </p><h2 class='highlight'>VERWENDUNG: </h2> <ol><li> Wählen Sie die Dateien aus, die Sie transkribieren lassen möchten (mehrere Dateien möglich)</li>" +
                "<li>  Wählen Sie ein Modell (<i>large</i> für das beste Resultat) und andere Parameter aus und klicken Sie auf 'Start'</li> <li>  Sehen Sie sich die entstandenen Transkripte im <i>transcripts</i>-Ordner dieses Verzeichnisses an </li></ol>",
                unsafe_allow_html=True)