from difflib import SequenceMatcher
from .openai_stt_api import transcribe_audio, save_audio
from fastapi import UploadFile



def compareText(audio_path, target_text):
    # 음성을 텍스트로 변환
    stt_text = transcribe_audio(audio_path, target_language="ko")

    # 문자열 유사성 계산
    similarity_ratio = SequenceMatcher(None, stt_text, target_text).ratio()
    
    return stt_text, similarity_ratio * 100

if __name__ == "__main__":
    # 음성 파일을 업로드하고 파일 경로를 저장
    uploaded_audio = UploadFile(...)
    audio_path = save_audio(uploaded_audio)
    
    # 비교 대상 텍스트 설정
    target_text = "안녕하세요"
    
    # 함수 호출하여 결과 저장
    transcribed_text, similarity_score = compareText(audio_path, target_text)

    # 변환된 텍스트 출력
    print("음성에서 변환된 텍스트:")
    print(transcribed_text)

    # 유사도 점수 출력
    print("음성과 대상 텍스트 출력 유사성:", similarity_score)