# SearchAndRescue

SearchAndRescue is an autonomous vehicle project developed for HackIllinois in collaboration with John Deere. It uses computer vision to detect humans in disaster scenarios, while avoiding animals and other obstacles. When a human is detected, the system sends a notification to rescue teams for timely assistance.

## Features

- **Autonomous Navigation**: Vehicle autonomously navigates disaster zones.
- **Human Detection**: Uses computer vision (OpenCV and TensorFlow) to detect humans.
- **Animal Avoidance**: Differentiates between humans and animals to prevent false alarms.
- **Rescue Notifications**: Sends notifications to rescue helpers when a human is found.

## Technologies Used

- Python
- OpenCV
- TensorFlow
- Autonomous Vehicle Integration

## How to Run

1. **Clone the repository**:
- git clone https://github.com/your-username/SearchAndRescue.git
- cd SearchAndRescue
- python -m venv venv
- source venv/bin/activate   # On Windows: venv\Scripts\activate
- pip install -r requirements.txt
- python main.py
