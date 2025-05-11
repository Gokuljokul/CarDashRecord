import cv2
import datetime
import time

def record_video(output_filename, duration_minutes=10):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))

    start_time = time.time()
    end_time = start_time + duration_minutes * 60

    while time.time() < end_time:
        ret, frame = cap.read()
        if not ret:
            break
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, current_datetime, (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.05)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    while True:
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"/mnt/media/recorded_video_{current_datetime}.avi"
        record_video(output_filename, duration_minutes=10)
        time.sleep(0.05)