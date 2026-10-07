import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time

from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.markdown(f"<h3 style='color: #31333F;'>Welcome, {student_data['name']} </h3>", unsafe_allow_html=True)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data 
            st.rerun()


    st.space()

    c1, c2 =st.columns(2)
    with c1:
        st.markdown("<h2 style='color: #31333F;'>Your Enrolled Subjects</h2>", unsafe_allow_html=True)
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()


    st.divider()


    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total":0, "attended": 0}

        stats_map[sid]['total'] +=1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1


    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']


        stats = stats_map.get(sid,{"total":0, "attended": 0} )
        def unenroll_button(current_sid=sid, current_sub_name=sub['name']):
            if st.button("Unenroll from this course", key=f"unenroll_{current_sid}", type='tertiary', width='stretch', icon=':material/delete_forever:'):
                unenroll_student_to_subject(student_id, current_sid)
                st.toast(f'Unenrolled from {current_sub_name} successfully!')
                st.rerun()

        with cols[i % 2]:

            subject_card(
                name = sub['name'],
                code =sub['subject_code'],
                section = sub['section'],
                stats = [
                    ('📅', 'Classes', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=unenroll_button
            )
    footer_dashboard()


def student_screen():


    style_background_dashboard()
    style_base_layout()


    if "student_data" in st.session_state:
        student_dashboard()
        return
    
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.markdown("<h2 style='text-align: center; color: #31333F;'>Login using FaceID</h2>", unsafe_allow_html=True)
    st.space()
    st.space()
    
    show_registration = False
    st.markdown("<p style='color: #31333F; font-size: 14px;'>Position your face in the center</p>", unsafe_allow_html=True)
    photo_source = st.camera_input("Position your face in the center", label_visibility="hidden")
    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')
            elif num_faces >1:
                st.warning('Multiple faces found')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id']==student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f'Welcome Back {student['name']}')
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('Face not recognized! You might be a new student!')
                    show_registration = True
    if show_registration:
        st.markdown("""
        <style>
            div[data-testid="stTextInput"] input {
                background-color: #ffffff !important;
                color: #31333F !important;
                border: 1.5px solid #c8cad4 !important;
                border-radius: 8px !important;
            }
            div[data-testid="stTextInput"] label {
                color: #31333F !important;
                font-weight: 600 !important;
                font-size: 14px !important;
            }
            div[data-testid="stTextInput"] input::placeholder {
                color: #9ea3b0 !important;
            }
        </style>
        """, unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<h2 style='color: #31333F;'>Register new Profile</h2>", unsafe_allow_html=True)
            new_name = st.text_input("Enter your name", placeholder='E.g. Hamza Rizvi')

            st.markdown("<h4 style='color: #31333F; margin-top: 8px;'>Optional : Voice Enrollment</h4>", unsafe_allow_html=True)
            st.info("Enroll your voice for voice-only attendance")


            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like I am present, My name is Akash.')
            except Exception:
                st.error('Audio Data failed!')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings= get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Couldnt capture your facial features for registration')

                else:
                    st.warning('Please enter your name!')


        
    footer_dashboard()