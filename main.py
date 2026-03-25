import cv2
import numpy as np
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def mark_attendance(name, status):
    time = datetime.now().strftime('%H:%M:%S')
    date = datetime.now().strftime('%Y-%m-%d')

    df = pd.DataFrame([[name, date, time, status]],
                      columns=["Name", "Date", "Time", "Status"])

    df.to_csv('attendance.csv', mode='a', header=False, index=False)

def start_recognition(mode):
    cam = cv2.VideoCapture(0)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x,y,w,h) in faces:
            id, conf = recognizer.predict(gray[y:y+h,x:x+w])

            if conf < 70:
                name = f"User_{id}"
                mark_attendance(name, mode)

                cv2.putText(img, f"{name} {mode}", (x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success", f"{name} {mode} marked!")
                return
            else:
                cv2.putText(img, "Unknown", (x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.imshow('Recognition', img)

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

# GUI
root = tk.Tk()
root.title("Face Attendance System")
root.geometry("400x300")

tk.Label(root, text="Face Attendance System", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Check IN", width=20,
          command=lambda: start_recognition("IN")).pack(pady=10)

tk.Button(root, text="Check OUT", width=20,
          command=lambda: start_recognition("OUT")).pack(pady=10)

tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=20)

root.mainloop()
