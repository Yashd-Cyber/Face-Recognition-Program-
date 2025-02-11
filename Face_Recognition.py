import face_recognition
import cv2

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
known_image = face_recognition.load_image_file("known_face.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Create an array of known face encodings and their corresponding names
known_face_encodings = [known_face_encoding]
known_face_names = ["Person 1"]  # Add the name of the person you want to recognize

# Initialize variables for face recognition
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Resize the frame of video to 1/4 size for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (OpenCV format) to RGB color (face_recognition format)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame to save time
    if process_this_frame:
        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Check if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"
            # If a match was found in known_face_encodings, use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale the face locations back up to the original frame size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Label the face
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit the video feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
