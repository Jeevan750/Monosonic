# Monosonic

**A webcam-based music player that connects facial-expression predictions to a local playlist.**

Monosonic combines OpenCV, DeepFace, and Pygame in a Python desktop prototype. Capture a frame from your webcam, predict an expression label, and play tracks from a matching CSV playlist.

## At a glance

| Component | Role |
| :--- | :--- |
| OpenCV | Webcam preview and image capture |
| DeepFace | Facial-expression prediction |
| pandas | Playlist loading from CSV files |
| Pygame | Local MP3 playback |
| keyboard | Playback shortcuts |

The current flow supports **happy, neutral, angry, and sad** expression labels. These are model predictions from an image, not a reliable measurement of a person's internal mood.

## How it works

1. Open the webcam preview and press **Space** to capture a frame.
2. DeepFace analyzes the saved image and returns an expression prediction.
3. The app loads the corresponding playlist from `song list/`.
4. Pygame plays local MP3 files, with keyboard controls for navigation.

## Getting started

The original application is designed around **Windows**, Python, a webcam, and an audio output device. Dependency versions are not pinned, so setup may require compatibility adjustments with newer packages.

Clone the repository and open a terminal in its root folder:

```sh
git clone https://github.com/Jeevan750/Monosonic.git
cd Monosonic
```

Create and activate a virtual environment in Windows Command Prompt, then install the libraries used by the source:

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install opencv-python deepface pygame keyboard pandas
python main.py
```

The existing `setup.cmd` installs the same five direct dependencies. `Monosonic.cmd` launches `main.py`; run it from the project folder after activating the environment.

## Controls

| Screen | Key | Action |
| :--- | :--- | :--- |
| Webcam preview | **Space** | Capture a frame for analysis |
| Music player | **P** | Pause |
| Music player | **R** | Resume |
| Music player | **D** | Next track |
| Music player | **A** | Previous track |
| Music player | **X** | Exit |

To try playback without webcam analysis, run `python player.py`. This separate player uses the neutral playlist.

## Files and playlists

| Path | Purpose |
| :--- | :--- |
| `main.py` | Webcam capture, expression analysis, and music playback |
| `player.py` | Standalone player using the neutral playlist |
| `song list/` | `happy.csv`, `neutral.csv`, `angry.csv`, and `sad.csv` playlists |
| `songs/` | Local MP3 files referenced by the playlists |
| `setup.cmd` | Dependency installation commands |
| `Monosonic.cmd` | Windows launch command |

Playlist CSV files contain three columns in this order: song name, artist, and album. The song name must match the MP3 filename without its extension:

```csv
Song,artist,album
Example Track,Example Artist,Example Album
```

That row resolves to `songs/Example Track.mp3`.

## Prototype notes

- The webcam capture is written to `opencv_frame_0.jpg` in the project folder and is not automatically deleted.
- The code expects `DeepFace.analyze()` to return a dictionary containing `dominant_emotion`. If an installed version returns a list, the result handling needs adapting.
- The capture flow retries labels outside the four supported playlists. Face-detection errors are not handled in the current script.
- Camera failure or pressing Escape before analysis can leave the result undefined. Playback also assumes that the playlist and audio files exist.
- Previous-track handling in `main.py` needs an edge-case fix at the start of a playlist; the standalone player handles that boundary differently.

This repository preserves the original prototype. A dependency lockfile, more robust input handling, and a unified player are useful next steps.
