
from face_enrollment import enroll_face
from face_recognition_module import recognize_face

print("Offline Facial Recognition System")
print("1. Enroll Face")
print("2. Recognize Face")

choice = input("Choice: ")
if choice == "1":
    enroll_face()
elif choice == "2":
    recognize_face()
