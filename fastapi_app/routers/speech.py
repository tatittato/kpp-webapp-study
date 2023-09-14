from fastapi import APIRouter

router = APIRouter(
    tags=["Speech"],
    responses={404: {"description": "Not found"}},
)


@router.post("/speech/score")
async def get_score(
    photo: UploadFile = File(..., title="업로드사진 파일", description="업로드사진 파일"),
):
    pass



@router.post("/photo",
             response_model=Photo,
             summary='사진 업로드',
             description='<p>직접 촬영 혹은 앨범에서 선택한 사진을 업로드하는 API.</p>'
                         '<b>photo_type</b>'
                         '<ol>'
                         '<li> ANYTHING : 스토리 일상</li>'
                         '<li> PLANT : 스토리 식물</li>'
                         '<li> GARDEN : 스토리 정원</li>'
                         '<li> DISEASE : 병충해의 병해</li>'
                         '<li> PEST : 병충해의 해충</li>'
                         '<li> DETAIL : 스토리 정원의 재촬영 사진</li>'
                         '<li> USER : 사용자 프로필</li>'
                         '<li> FM : 나눔장터</li>'
                         '<li> QNA : 질문하기</li>'
                         '<li> CS : 1:1 질문하기</li>'
                         '<li> PLANT_DT : 식물 사전</li>'
                         '<li> DNP_DT : 병충해 사전</li>'
                         '<li> ADMIN : 기획 컨텐츠</li>'
                         '</ol>'
                         '<b>사용처</b>'
                         '<ol>'
                         '<li>카메라 > 식물 > 촬영</li>'
                         '<li>카메라 > 정원 > 촬영</li>'
                         '<li>카메라 > 병충해 > 촬영</li>'
                         '<li>카메라 > 해충 > 촬영</li>'
                         '</ol>')
async def upload_photo(
        photo: UploadFile = File(..., title="업로드사진 파일", description="업로드사진 파일"),
        photo_type: str = Form(..., title="사진 종류", enum=K.PHOTO_TYPES, description="사진 종류"),
        image_width: int = Form(..., title="원본 이미지 width", ge=1, example=1024, description="원본 이미지 width"),
        image_height: int = Form(..., title="원본 이미지 height", ge=1, example=768, description="원본 이미지 height"),
        device_id: str = Form(None, title="디바이스 id(fcm token)", description="디바이스 id(fcm token, 로그인 안된 경우 사용)"),
        content_id: int = Form(None, title="content id",
                               description="content id(컨텐츠를 먼저 저장한 후에 사진을 업로드할 경우에만 사용할 필드)"),
        only_save_original: bool = Form(False, title="원본 이미지만 저장할 지 여부", description="원본 이미지만 저장할지 여부(썸네일 저장 안함)"),
        auth_user_id: int = Header(None, title="사용자 아이디", ge=1, example=1, description="사용자 아이디"),
        db: Session = Depends(get_db)
):
    if C.ENABLE_MOCK_DATA:
        return {"photo_id": 1}

    photo = image_manager.convert_bytes_to_pil_im(await photo.read())
    photo_id = _upload_photo(photo_type, image_width, image_height, auth_user_id, device_id, content_id, photo, db,
                             only_save_original)
    if not isinstance(photo_id, int):
        return photo_id

    db.commit()

    return {"photo_id": photo_id}
#test