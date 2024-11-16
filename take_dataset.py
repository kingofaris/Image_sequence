import cv2
import os
import time
import csv

# Path untuk menyimpan dataset
dataset_path = "dataset"
images_path = os.path.join(dataset_path, "images")
timestamps_path = os.path.join(dataset_path, "timestamps.txt")
csv_path = os.path.join(dataset_path, "images.csv")

# Buat folder jika belum ada
os.makedirs(images_path, exist_ok=True)

# Buka file timestamps.txt dan data.csv untuk menulis
with open(timestamps_path, "w") as timestamp_file, open(csv_path, mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Tulis header untuk data.csv
    csv_writer.writerow(["#timestamp [ns]", "filename"])

    # Menggunakan kamera atau video
    cap = cv2.VideoCapture('recorded_video_Original_FisheyeView_20241113_162551.avi')  # gunakan `("video.mp4")` jika ingin dari video

    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Nama file gambar tanpa ekstensi
        image_filename = f"{frame_id:06d}"
        image_file = f"{image_filename}.png"
        image_path = os.path.join(images_path, image_file)

        # Simpan gambar
        cv2.imwrite(image_path, frame)

        # Tulis nama file gambar tanpa ekstensi ke timestamps.txt
        timestamp_file.write(f"{image_filename}\n")

        # Tulis nama file gambar tanpa ekstensi dan nama file lengkap ke data.csv
        csv_writer.writerow([image_filename, image_file])

        # Tampilkan frame untuk memastikan berjalan
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        frame_id += 1

    cap.release()
    cv2.destroyAllWindows()

