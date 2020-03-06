import face_recognition as fr

curr = fr.load_image_file('known/Bill Gates.jfif')
curr_encoding = fr.face_encodings(curr)[0]
prev = fr.load_image_file('unknown/BG_u.jfif')
prev_encoding = fr.face_encodings(prev)[0]
result = fr.compare_faces([curr_encoding], prev_encoding)

if result[0]:
    print("The two faces match")
else:
    print("Not Matched!!!")