This directory is an extension that provides methods to use obscurity as a metric in order to improve guessing in quiz-bowl.

preprocess.py should be ran one-time to collect/pickle information necessary to retrieve obscurity results in a fast manner.
obscurity.py is the actual API called by the QANTA system to figure out obscurity metrics.
