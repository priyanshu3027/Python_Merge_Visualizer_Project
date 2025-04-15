📊 Merge Sort Visualizer – Enhanced (Pygame)
A dynamic and visually appealing Merge Sort visualizer created using Python and Pygame. This project animates the step-by-step execution of the Merge Sort algorithm, helping learners understand the divide-and-conquer approach through interactive graphics.

🧠 Project Overview
Sorting algorithms can be abstract and hard to grasp through code alone. This visualizer bridges that gap by showing each operation visually—dividing, comparing, merging, and finally sorting elements in an animated format.

🚀 Features
🎨 Color-coded Visuals:

Green – Initial unsorted state

Orange – Comparing elements

Blue – Swapping/Merging values

Light Green – Sorted part of the array

Purple – Final sorted result

🧩 User Interactions:

Press Enter to begin Merge Sort.

Press R to reset the array with new random values.

📈 Real-time Rendering:

Animated transitions

Smooth rendering of sorting steps

📂 Project Structure
bash
Copy
Edit
merge_sort_visualizer/
│
├── merge_sort_visualizer.py   # Main application code
├── README.md                  # Project documentation (you are here!)
🛠️ Technologies Used
Language: Python 3.x

Graphics Library: Pygame

IDE: VS Code / PyCharm (recommended)

💡 How It Works
A random array is generated with heights mapped to bar lengths.

Merge Sort recursively divides and merges the array.

Visual feedback is provided with color transitions at each step.

Once sorted, all bars turn purple to indicate completion.

🔧 Setup Instructions
Prerequisites:
Python 3.x installed

Pygame installed via pip

bash
Copy
Edit
pip install pygame
Run the Visualizer:
bash
Copy
Edit
python merge_sort_visualizer.py
🧪 Sample Code Snippet
python
Copy
Edit
if event.key == pygame.K_RETURN and not sorting:
    sorting = True
    merge_sort(1, NUM_BARS)
This snippet triggers the sorting animation when the Enter key is pressed.

🔄 Future Enhancements
Add sorting algorithm selector (e.g., Quick Sort, Bubble Sort).

Include speed control (slow, medium, fast).

Allow custom input for array values.

Add pause/resume functionality.

Display step count or time taken.

🧠 Educational Value
This project is ideal for:

CS students learning sorting algorithms

Beginners practicing Python and visual programming

Educators explaining Divide and Conquer visually

📜 License
This project is open-source and free to use for educational or personal purposes.

🙌 Acknowledgments
Inspired by algorithm visualizers from GeeksforGeeks and VisuAlgo

Built with ❤️ using Python and Pygame
