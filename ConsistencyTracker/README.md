# Habit Tracker - README

## Overview

The Habit Tracker is a simple Python application that allows users to track their daily habits. It uses SQLite to store habit logs and provides a variety of features, including habit logging, streak tracking, and data visualization.

## Features

- **Log a Habit**: Track a specific habit on a given day.
- **Check Streak**: Check how many consecutive days you've kept up with a particular habit.
- **Visualize Habit Progress**: View a graph displaying the progress of your habit over time.
- **List Habits**: View a list of all the habits you've tracked.

## Requirements

- Python 3.x
- `matplotlib` library for visualizing data
- `sqlite3` (included in Python standard library)

## Installation

1. Clone or download the repository to your local machine.
2. Install required Python libraries:

    ```bash
    pip install matplotlib
    ```

3. Run the script:

    ```bash
    python habit_tracker.py
    ```

## Usage

Upon running the script, you'll be presented with a menu that allows you to:

1. **Log a habit**: 
    - Select option 1 and enter the name of the habit you want to track.
    
2. **Check streak**: 
    - Select option 2 and enter the habit name to see your current streak (consecutive days).

3. **Visualize habit progress**: 
    - Select option 3 and enter the habit name to view a graph of your habit progress over time.

4. **List habits**: 
    - Select option 4 to see all the habits you've logged.

5. **Exit**: 
    - Select option 5 to exit the application.

## Example of Use

1. **Log a Habit**: 
    - Select option 1, enter "Exercise", and it will log the habit for today's date.

2. **Check Streak**:
    - Select option 2, enter "Exercise", and it will show how many consecutive days you’ve exercised.

3. **Visualize Progress**:
    - Select option 3, enter "Exercise", and it will display a graph of your exercise streak.

4. **List Habits**: 
    - Select option 4 to see all tracked habits.
      

## Acknowledgments

- `matplotlib` for the data visualization
- SQLite for lightweight database storage
