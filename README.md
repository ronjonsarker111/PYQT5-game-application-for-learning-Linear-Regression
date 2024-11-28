# Linear Regression Estimator
This project is a PyQt5-based GUI application for learning linear regression through visualization and interactive controls. It allows users to generate and manipulate signals, add noise, and estimate linear regression parameters in an intuitive way.

## Features

- Generate a linear signal with user-controlled slope (`a`), intercept (`b`), and data points (`n`).
- Add noise to the signal using Gaussian or Uniform distribution.
- Interactive sliders for real-time adjustment of:
  - Signal parameters (`a`, `b`, `n`)
  - Noise properties (Mean, Sigma)
  - Histogram bin size for noise distribution.
- Visualize:
  - The initial linear signal.
  - Noisy signal and the estimated linear trend.
  - Noise and its distribution.
- Calculate and display:
  - Estimated parameters (`a`, `b`, `sigma`).
  - Errors between initial and estimated parameters.
  - Coefficient of determination (`R²`).

## Dependencies

The project requires the following Python packages:
- `PyQt5`
- `numpy`
- `matplotlib`

##To install dependencies, run:
```bash
pip install PyQt5 numpy matplotlib

##How to Run
Clone the repository:
git clone https://github.com/ronjonsarker111/PYQT5-game-application-for-learning-Linear-Regression.git
cd PYQT5-game-application-for-learning-Linear-Regression

## Run the application:
python main.py

## File Structure
main.py: The main application logic for the PyQt5 GUI.
projectDesign.py: Auto-generated PyQt5 UI Python file for the GUI design.
projectDesign.ui: The XML-based UI design file created using Qt Designer.

**Authors**
Boiko Andrii
Fatemeh Karamian Sorkhani
Sarker Modan Mohan


License: 
This project is licensed under the MIT License. See LICENSE for details.

You can modify the repository URL and any other details if needed. Let me know if you need help refining or expanding this!



