import cv2

def extract_clip(input_file, output_file, start_time, end_time):
    # Open the input video file
    video_capture = cv2.VideoCapture(input_file)
    
    # Check if the video file opened successfully
    if not video_capture.isOpened():
        print("Error: Unable to open video file.")
        return
    
    # Get the frame rate of the video
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    
    # Convert start and end times from seconds to frame numbers
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)
    
    # Set the starting frame
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    
    # Create a VideoWriter object to save the extracted clip
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    output_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (output_width, output_height))
    
    # Read frames from the input video and write them to the output clip
    frame_count = start_frame
    while frame_count <= end_frame:
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Unable to read frame.")
            break
        video_writer.write(frame)
        frame_count += 1
    
    # Release the video capture and writer objects
    video_capture.release()
    video_writer.release()
    
    print("Clip extraction complete.")

# Example usage:
input_file = 'input.mp4'
output_file = 'output_clip.mp4'
start_time = 10  # Start time of the clip in seconds
end_time = 20    # End time of the clip in seconds

extract_clip(input_file, output_file, start_time, end_time)
