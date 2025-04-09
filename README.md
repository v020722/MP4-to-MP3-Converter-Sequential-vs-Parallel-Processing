# MP4 to MP3 Converter – Sequential vs Parallel Processing

## 📝 Project Overview
This Python application converts `.mp4` video files to `.mp3` audio files by extracting the audio stream using the `moviepy` library. The purpose of the project is to compare the performance of **sequential** and **parallel processing** approaches using two different computer systems.

This project was developed as part of a **Computer Hardware** coursework assignment.

---

## 🎯 Objectives
- Convert multiple `.mp4` files to `.mp3` format.
- Measure and compare the execution time of **sequential** vs **parallel** conversion.
- Analyze performance differences across two laptops with different hardware specifications.

---

## 🛠️ Technologies Used
- **Language**: Python
- **IDE**: Visual Studio Code
- **Libraries**:
  - `os` – for file and folder operations
  - `time` – for execution time measurement
  - `moviepy.editor` – for video/audio processing
  - `concurrent.futures` – for parallel execution (used in the parallel version)

---

## 🧪 System Specifications Compared

| Feature | Vivobook (X421EQ_S433EQ) | Latitude 7480 |
|--------|----------------------------|----------------|
| CPU    | Intel i7-1165G7 (More cores) | Intel i7-7600U |
| RAM    | 2134 MHz | Slower RAM |
| Cores  | Higher count | Fewer cores |
| Outcome| Faster in both parallel and sequential | Slower in comparison |

---

## ⚙️ Program Structure

### `sequential.py`
- Processes MP4 files one after the other.
- Logs each conversion and total processing time.
- Slower but more consistent for smaller workloads.

### `parallel.py`
- Uses a thread pool to convert files concurrently.
- Significantly reduces overall time for larger batches.
- Demonstrates the benefit of multi-core systems.

---

## 📊 Performance Comparison

| Mode        | Vivobook | Latitude |
|-------------|----------|----------|
| Sequential  | 27.7s    | 30.0s    |
| Parallel    | 14.2s    | 15.1s    |

- Parallel processing cuts processing time by nearly half.
- Vivobook consistently outperforms Latitude due to superior specs.

---

## 🔄 How to Run

1. Install dependencies:
   ```bash
   pip install moviepy
   ```

2. Update the `input_folder` and `output_folder` paths in the scripts.

3. Run either script:
   ```bash
   python sequential.py
   # or
   python parallel.py
   ```

---

## 📌 Key Takeaways

- **Sequential** processing runs tasks one at a time – suitable for simple, single-thread workloads.
- **Parallel** processing takes advantage of multi-core CPUs for faster execution on large datasets.
- Parallelism is less beneficial for single-file processing due to IO limitations.

---

## 📽️ Demo
- Live demo on **Vivobook X421EQ**
- Recorded demo on **Latitude 7480**

---

## 👩‍💻 Author
**Vijeta d/o Senthil Nathan**
